import math
import itertools
import numpy as np
import pandas as pd
from classes import *
from pulp import *
import statistics
import scipy.optimize as optimize
import inspect

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    if type(val) != bool:
        return 'color: black'

    color = 'red' if val == True else 'black'
    return 'color: %s' % color

def color_positive_green(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    if type(val) != bool:
        return 'color: black'

    color = 'green' if val == True else 'black'
    return 'color: %s' % color

class ParlaySystem():
    def __init__(self, binaries, target_profit, bounds, binary_index_arr, binary_results_arr, index_to_ml={}, index_to_outcome={}, override_arr=[]):
        self.binaries = binaries
        self.lp_variables = {}
        self.all_parlays = []
        self.target_profit = target_profit
        self.bounds = bounds
        self.binary_index_arr = binary_index_arr
        self.binary_results_arr = binary_results_arr
        self.index_to_ml = index_to_ml
        self.index_to_outcome = index_to_outcome
        self.override_arr = override_arr

        self.create_parlay_system()

    def print_parlay_odds_diff(self):
        result = [0, 0]
        for binary in self.binaries:
            for ml in binary:
                if ml.odds >= 0:
                    result[0] += ml.odds
                else:
                    result[1] += ml.odds

        print('[ + , - ]: ', result)
        # print(' pos/neg :', result[0] / result[1])
        print('toalt_dif: ', sum(result))

    def select_flattened_prop(self, prop):
        np_binaries = np.array(self.binaries)
        np_binaries = np_binaries.flatten()
        return [getattr(bin, prop) for bin in np_binaries]

    def create_parlay_system(self):
        lst = list(itertools.product([i for i in range(len(self.binaries[0]))], repeat=len(self.binaries)))
        for tuple in lst:
            parlay = []
            parlay_name = []
            for j in range(len(tuple)):
                selection = tuple[j]
                money_line = self.binaries[j][selection]
                parlay.append(money_line)
                parlay_name.append(money_line.event)

            globals()["_".join(parlay_name)] = Parlay(money_line_arr=parlay, bet_amount=1)

            ### Handle an "override" situation given an index_arr that is to be overrided
            current_parlay = globals()["_".join(parlay_name)]
            # if sorted(current_parlay.index_arr) == sorted(self.override_arr):
            #     current_parlay.override_odds(1520)
            #     print("yooooo", current_parlay.event, current_parlay.index_arr, current_parlay.odds, current_parlay.multiplier)

            self.all_parlays.append(current_parlay)

    def slsqp_solver(self):

        def f(x):   # The rosenbrock function
            parlay_profits = []

            for i in range(len(x)):
                parlay = self.all_parlays[i]
                parlay.update_bet_amount(x[i])
                profit = parlay.payout - sum(x)
                parlay_profits.append(profit)

            # print("statistics.mean(parlay_profits): ", statistics.mean(parlay_profits))
            return -statistics.mean(parlay_profits)

        bnds = ()
        for i in range(len(self.all_parlays)):
            bnds += (self.bounds,)

        cons = [{'type': 'ineq', 'fun': lambda x, i=i : x[i] * self.all_parlays[i].multiplier - self.target_profit - sum(x) } for i in range(len(self.all_parlays))]

        # COBYLA doesn't support bounds in this format
        FinalVal= optimize.minimize(f, np.ones(len(self.all_parlays)), method='SLSQP', bounds=bnds, constraints=cons)
        print(FinalVal)

        events = []
        index_arrs = []
        results = []
        event_status_arr = []
        odds = []
        bets = []
        multipliers = []
        payouts = []
        profits = []

        for i in range(len(FinalVal.x)):
            solver_bet_amount = FinalVal.x[i]

            parlay = self.all_parlays[i]
            parlay.update_bet_amount(solver_bet_amount)

            index_arr = [str(i) for i in parlay.index_arr]
            result = [self.index_to_outcome[i] for i in parlay.index_arr]
            event_status = result.count(1) == len(result)
            event = parlay.event
            multiplier = parlay.multiplier
            payout = parlay.payout
            profit = parlay.bet_amount * parlay.multiplier - sum(FinalVal.x)

            index_arrs.append(index_arr)
            results.append(result)
            event_status_arr.append(event_status)
            odds.append(parlay.odds)
            events.append(event)
            bets.append(round(parlay.bet_amount, 4))
            multipliers.append(multiplier)
            payouts.append(round(payout, 4))
            profits.append(round(profit, 3))

        df = pd.DataFrame({'event': events,
                           'index[]': index_arrs,
                           'result': results,
                           'ev_stat': event_status_arr,
                           'odds': odds,
                           'bet': bets,
                           'mult': multipliers,
                           'payout': payouts,
                           'profit': profits
                            })
        df = df.sort_values(by=['ev_stat', 'profit'], ascending=[False, False])

        total_bet = round(sum(bets), 2)
        print('slsqp_solver: ')
        print(df)
        print('total_bet   : ', total_bet)
        print('mean        : ', df["profit"].mean())
        print('max         : ', df["profit"].max())
        print('min         : ', df["profit"].min())
        print('std         : ', df["profit"].std())
        print(df.describe())
        self.print_parlay_odds_diff()
        csv_data = [index_arr, total_bet, df["profit"].mean(), df["profit"].std(), df["profit"].max(), df["profit"].min()]
        return csv_data, df


    def lp_solver(self):
        prob = LpProblem("Example_Problem", LpMaximize)

        for parlay in self.all_parlays:
            self.lp_variables[parlay.event] = LpVariable(name=parlay.event, lowBound=1, cat="Continuous")

        opt = 0
        all_bets_sum = 0
        # Set up optimization function and total bet amount
        for parlay in self.all_parlays:
            lp_var = self.lp_variables[parlay.event]
            opt += (lp_var * parlay.multiplier)
            all_bets_sum += lp_var

        print("opt: ", opt)
        print("all_bets_sum: ", all_bets_sum)

        prob += all_bets_sum / len(self.all_parlays)

        # Set up constraints to be added to problem
        for parlay in self.all_parlays:
            lp_var = self.lp_variables[parlay.event]
            prob += (lp_var * parlay.multiplier + lp_var) - all_bets_sum >= self.target_profit

        prob.solve()

        print("Status:", LpStatus[prob.status])
        # Each of the variables is printed with it's resolved optimum value
        total_bet_amount = 0
        for v in prob.variables():
            total_bet_amount += v.varValue


        events = []
        bets = []
        multipliers = []
        payouts = []
        profits = []

        for v in prob.variables():
            for p in self.all_parlays:
                if p.event == v.name:
                    val = v.varValue
                    parlay = p
                    event = parlay.event
                    multiplier = parlay.multiplier
                    payout = val * parlay.multiplier
                    profit = val * parlay.multiplier - total_bet_amount

                    events.append(event)
                    bets.append(round(val, 4))
                    multipliers.append(multiplier)
                    payouts.append(round(payout, 4))
                    profits.append(round(profit, 4))

        df = pd.DataFrame({'event': events,
                           'bet': bets,
                           'multiplier': multipliers,
                           'payout': payouts,
                           'profit': profits
                            })
        print('lp_solver: ')
        print(df)

    def export_to_csv(self):
        csv_data = []
        for parlay in self.all_parlays:
            csv_data.append(parlay.format_stats_for_csv())

        print("\n".join(csv_data))
