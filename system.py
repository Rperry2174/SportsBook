import math
import itertools
import numpy as np
from classes import *
from pulp import *
import statistics
import scipy.optimize as optimize
import inspect



# Create the 'prob' variable to contain the problem data

broncos = MoneyLine(event="broncos", bet_amount=100, odds=440)
texans = MoneyLine(event="texans", bet_amount=100, odds=128)
dolphins = MoneyLine(event="dolphins", bet_amount=100, odds=148)
#
chiefs = MoneyLine(event="chiefs", bet_amount=100, odds=-560)
titans = MoneyLine(event="titans", bet_amount=100, odds=-157)
giants = MoneyLine(event="giants", bet_amount=100, odds=-182)

broncos.print_stats()
texans.print_stats()
dolphins.print_stats()
#
chiefs.print_stats()
titans.print_stats()
giants.print_stats()

class System():
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
                money_line = binaries[j][selection]
                parlay.append(money_line)
                parlay_name.append(money_line.event)

            globals()["_".join(parlay_name)] = Parlay(money_line_arr=parlay, bet_amount=1)
            self.all_parlays.append(globals()["_".join(parlay_name)])

    def solver(self):

        def f(x):   # The rosenbrock function
            parlay_returns = []

            for i in range(len(x)):
                parlay = self.all_parlays[i]
                parlay_returns.append((x[i] * parlay.multiplier + x[i]) - sum(x))

            # print("statistics.mean(parlay_returns): ", statistics.mean(parlay_returns))
            return -statistics.mean(parlay_returns)

        bnds = ()
        cons2 = []
        for i in range(len(self.all_parlays)):
            parlay = self.all_parlays[i]

            print("parlay.multiplier: ", parlay.multiplier)

            bnds += ((1, 30),)
            cons2.append({'type': 'ineq', 'fun': lambda x: x[i] * parlay.multiplier + x[i] - sum(x) - 1 })
            # cons += (({'type': 'ineq', 'fun': lambda x: x[i] - 1 },))

        cons3 = [{'type': 'ineq', 'fun': lambda x, i=i : x[i] * self.all_parlays[i].multiplier + x[i] - sum(x) - 1 } for i in range(len(self.all_parlays))]

        cons = [{'type': 'ineq', 'fun': lambda x: x[0]*30.533760000000008+x[0] - (x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7]) - 1 },
                {'type': 'ineq', 'fun': lambda x: x[1]*19.07683516483517+x[1] - (x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7]) - 1 },
                {'type': 'ineq', 'fun': lambda x: x[2]*21.921936305732483+x[2] - (x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7]) - 1 },
                {'type': 'ineq', 'fun': lambda x: x[3]*13.696353328200463+x[3] - (x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7]) - 1 },
                {'type': 'ineq', 'fun': lambda x: x[4]*6.664114285714287+x[4] - (x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7]) - 1 },
                {'type': 'ineq', 'fun': lambda x: x[5]*4.163594976452121+x[5] - (x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7]) - 1 },
                {'type': 'ineq', 'fun': lambda x: x[6]*4.784549590536852+x[6] - (x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7]) - 1 },
                {'type': 'ineq', 'fun': lambda x: x[7]*2.989283464488196+x[7] - (x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7]) - 1 }]

        print("bmds:", bnds)
        # print("cons:", inspect.getsource(cons[1]['fun']))
        print("cons:", cons)
        print("cons2:", cons2)
        print("cons3:", cons3)

        # COBYLA doesn't support bounds
        FinalVal= optimize.minimize(f, [2, 2, 2, 2, 2, 2, 2, 2], method='SLSQP', bounds=bnds, constraints=cons)
        print(FinalVal)

        for i in range(len(FinalVal.x)):
            val = FinalVal.x[i]
            parlay = self.all_parlays[i]
            event = parlay.event
            multiplier = parlay.multiplier
            payout = val * parlay.multiplier
            profit = val * parlay.multiplier - sum(FinalVal.x)

            print('==')

            print('event: ', event)
            print('val: ', val)
            print('multiplier: ', multiplier)
            print('payout: ', payout)
            print('profit: ', profit)
            print('all_bets:', sum(FinalVal.x))
            print('==')

        test = 3
        print('ans', cons[test]['fun']([1, 1, 1, 1, 1.76884686, 2.2068189 , 2.05533119, 2.66535638]))
        print('ans2', cons2[test]['fun']([1, 1, 1, 1, 1.76884686, 2.2068189 , 2.05533119, 2.66535638]))
        print('ans3', cons3[test]['fun']([1, 1, 1, 1, 1.76884686, 2.2068189 , 2.05533119, 2.66535638]))


    # def solver(self):
    #     prob = LpProblem("Example_Problem", LpMaximize)
    #
    #     for parlay in self.all_parlays:
    #         self.lp_variables[parlay.event] = LpVariable(name=parlay.event, lowBound=1, cat="Continuous")
    #
    #     opt = 0
    #     all_bets_sum = 0
    #     # Set up optimization function and total bet amount
    #     for parlay in self.all_parlays:
    #         lp_var = self.lp_variables[parlay.event]
    #         opt += (lp_var * parlay.multiplier + lp_var)
    #         all_bets_sum += lp_var
    #
    #     print("opt: ", opt)
    #     print("all_bets_sum: ", all_bets_sum)
    #
    #     prob += all_bets_sum / 8.0
    #
    #     # Set up constraints to be added to problem
    #     for parlay in self.all_parlays:
    #         lp_var = self.lp_variables[parlay.event]
    #         prob += (lp_var * parlay.multiplier + lp_var) - all_bets_sum >= 1
    #
    #     prob.solve()
    #
    #     print("Status:", LpStatus[prob.status])
    #     # Each of the variables is printed with it's resolved optimum value
    #     total_bet_amount = 0
    #     for v in prob.variables():
    #         total_bet_amount += v.varValue
    #
    #     for v in prob.variables():
    #         for p in self.all_parlays:
    #             if p.event == v.name:
    #                 print(v.name, "bet=", v.varValue, "\n", "profit: ", v.varValue * p.multiplier - total_bet_amount)

    def export_to_csv(self):
        csv_data = []
        for parlay in self.all_parlays:
            csv_data.append(parlay.format_stats_for_csv())

        print("\n".join(csv_data))


binaries = [[broncos, chiefs], [texans, titans], [dolphins, giants]]
s = System(binaries=binaries)
s.solver()


# def f2(num_options):
#     f = np.zeros(num_options)
