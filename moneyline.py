import math
import itertools
import numpy as np
from classes import *

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

    def select_flattened_prop(self, prop):
        np_binaries = np.array(self.binaries)
        np_binaries = np_binaries.flatten()
        print([getattr(bin, prop) for bin in np_binaries])

    def export_to_csv(self):
        lst = list(itertools.product([0, 1], repeat=len(self.binaries)))

        all_parlays = []
        for tuple in lst:
            parlay = []
            parlay_name = []
            for j in range(len(tuple)):
                selection = tuple[j]
                money_line = binaries[j][selection]
                parlay.append(money_line)
                parlay_name.append(money_line.event)

            globals()["_".join(parlay_name)] = Parlay(money_line_arr=parlay, bet_amount=1)
            all_parlays.append(globals()["_".join(parlay_name)])

        # print(all_parlays[0].odds)
        csv_data = []
        for parlay in all_parlays:
            csv_data.append(parlay.format_stats_for_csv())

        print("\n".join(csv_data))


binaries = [[broncos, chiefs], [texans, titans], [dolphins, giants]]
s = System(binaries=binaries)
s.select_flattened_prop('event')


# def f2(num_options):
#     f = np.zeros(num_options)
