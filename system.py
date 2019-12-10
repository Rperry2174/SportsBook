import math
import itertools
import numpy as np
from classes import *
from pulp import *

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
        prob = LpProblem("Example_Problem", LpMaximize)

        for parlay in self.all_parlays:
            self.lp_variables[parlay.event] = LpVariable(name=parlay.event, lowBound=1, cat="Continuous")

        opt = 0
        all_bets_sum = 0
        # Set up optimization function and total bet amount
        for parlay in self.all_parlays:
            lp_var = self.lp_variables[parlay.event]
            opt += (lp_var * parlay.multiplier + lp_var)
            all_bets_sum += lp_var

        print("opt: ", opt)
        print("all_bets_sum: ", all_bets_sum)

        prob += all_bets_sum / 8.0

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

        for v in prob.variables():
            for p in self.all_parlays:
                if p.event == v.name:
                    print(v.name, "bet=", v.varValue, "\n", "profit: ", v.varValue * p.multiplier - total_bet_amount)

    def export_to_csv(self):
        csv_data = []
        for parlay in self.all_parlays:
            csv_data.append(parlay.format_stats_for_csv())

        print("\n".join(csv_data))


binaries = [[broncos, chiefs], [texans, titans], [dolphins, giants]]
s = System(binaries=binaries)
s.solver()
print(s.lp_variables)
print(s.all_parlays)


# def f2(num_options):
#     f = np.zeros(num_options)
