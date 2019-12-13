import math
import itertools
import numpy as np
import pandas as pd
from classes import *
from pulp import *
import statistics
import scipy.optimize as optimize
import inspect

class ParlaySystem():
    def __init__(self, binaries):
        self.binaries = binaries
        self.lp_variables = {}
        self.all_parlays = []
        self.create_parlay_system()

    def select_flattened_prop(self, prop):
        np_binaries = np.array(self.binaries)
        np_binaries = np_binaries.flatten()
        return [getattr(bin, prop) for bin in np_binaries]

    def create_parlay_system(self):
        lst = list(itertools.product([0, 1], repeat=len(self.binaries)))

        for tuple in lst:
            parlay = []
            parlay_name = []
            for j in range(len(tuple)):
                selection = tuple[j]
                money_line = self.binaries[j][selection]
                parlay.append(money_line)
                parlay_name.append(money_line.event)

            globals()["_".join(parlay_name)] = Parlay(money_line_arr=parlay, bet_amount=1)
            self.all_parlays.append(globals()["_".join(parlay_name)])

    def slsqp_solver(self):

        def f(x):   # The rosenbrock function
            parlay_returns = []

            for i in range(len(x)):
                parlay = self.all_parlays[i]
                parlay_returns.append((x[i] * parlay.multiplier + x[i]) - sum(x))

            # print("statistics.mean(parlay_returns): ", statistics.mean(parlay_returns))
            return -statistics.mean(parlay_returns)

        bnds = ()
        for i in range(len(self.all_parlays)):
            bnds += ((1, 30),)

        cons = [{'type': 'ineq', 'fun': lambda x, i=i : x[i] * self.all_parlays[i].multiplier - sum(x) - 1 } for i in range(len(self.all_parlays))]

        # COBYLA doesn't support bounds in this format
        FinalVal= optimize.minimize(f, np.ones(len(self.all_parlays)), method='SLSQP', bounds=bnds, constraints=cons)
        print(FinalVal)

        events = []
        bets = []
        multipliers = []
        payouts = []
        profits = []

        for i in range(len(FinalVal.x)):
            val = FinalVal.x[i]
            parlay = self.all_parlays[i]
            event = parlay.event
            multiplier = parlay.multiplier
            payout = val * parlay.multiplier
            profit = val * parlay.multiplier - sum(FinalVal.x)

            events.append(event)
            bets.append(val)
            multipliers.append(multiplier)
            payouts.append(payout)
            profits.append(round(profit, 4))

        df = pd.DataFrame({'event': events,
                           'bet': bets,
                           'multiplier': multipliers,
                           'payout': payouts,
                           'profit': profits
                            })
        print('slsqp_solver: ')
        print(df)


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
            prob += (lp_var * parlay.multiplier + lp_var) - all_bets_sum >= 1

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
                    bets.append(val)
                    multipliers.append(multiplier)
                    payouts.append(payout)
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
