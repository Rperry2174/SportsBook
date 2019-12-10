import math
import itertools
import numpy as np

class MoneyLine():
    def __init__(self, event, bet_amount, odds):
        self.event = event
        self.bet_amount = bet_amount
        self.odds = odds
        self.multiplier = self.calculate_multiplier()
        self.payout = self.calculate_payout()

    def calculate_multiplier(self):
        if self.odds > 0:
            return 1 + (self.odds / 100.0)
        else:
            return 1 + (100.0 / abs(self.odds))

    def calculate_payout(self):
        return self.multiplier * self.bet_amount


    def print_stats(self):
        print("=========================")
        print("event: ", self.event)
        print("bet_amount: ", self.bet_amount)
        print("odds: ", self.odds)
        print("multiplier: ", self.multiplier)
        print("payout:" , self.payout)
        print("=========================")



# giants = MoneyLine(event="giants", bet_amount=100, odds=-150)
# dolphins = MoneyLine(event="dolphins", bet_amount=100, odds=170)
# rangers = MoneyLine(event="rangers", bet_amount=100, odds=-120)
# print(giants.print_stats())
# print(dolphins.print_stats())
# print(rangers.print_stats())

class Parlay():
    def __init__(self, money_line_arr, bet_amount):
        self.money_line_arr = money_line_arr
        self.event = self.format_events()
        self.bet_amount = bet_amount
        self.multiplier = self.calculate_multiplier()
        self.payout = self.calculate_payout()
        self.odds = self.derive_odds()

    def calculate_multiplier(self):
        parlay_multiplier = 1
        for ml in self.money_line_arr:
            parlay_multiplier *= ml.multiplier

        return parlay_multiplier

    # OFF BY ONE....
    def calculate_payout(self):
        return self.multiplier * self.bet_amount

    def format_events(self):
        result = ""
        for ml in self.money_line_arr:
            result += ml.event + "_"

        return result

    def derive_odds(self):
        return 100.0 * ((self.payout / self.bet_amount) - 1.0)

    def format_stats_for_csv(self):
        items = [self.event, str(self.bet_amount), str(self.odds), str(self.payout)]
        return ",".join(items)

    def print_stats(self):
        print("=========================")
        print("event: ", self.event)
        print("bet_amount: ", self.bet_amount)
        print("odds: ", self.odds)
        print("multiplier: ", self.multiplier)
        print("payout:" , self.payout)
        print("=========================")

# parlay = Parlay([giants, dolphins, rangers], 1)
# parlay.print_stats()

# steelers = MoneyLine(event="steelers", bet_amount=100, odds=-129)
# patriots = MoneyLine(event="patriots", bet_amount=100, odds=-157)
# titans = MoneyLine(event="titans", bet_amount=100, odds=-157)
#
# steelers.print_stats()
# patriots.print_stats()
# titans.print_stats()

# parlay1 = Parlay(money_line_arr=[steelers,patriots,titans], bet_amount=1)
# parlay1.print_stats()

# cardinals = MoneyLine(event="cardinals", bet_amount=100, odds=114)
# raiders = MoneyLine(event="raiders", bet_amount=100, odds=138)
# chiefs = MoneyLine(event="chiefs", bet_amount=100, odds=138)
#
# cardinals.print_stats()
# raiders.print_stats()
# chiefs.print_stats()

# parlay2 = Parlay(money_line_arr=[cardinals,chiefs, raiders], bet_amount=1)
# parlay2.print_stats()

# binaries = [[steelers, cardinals], [patriots, chiefs], [titans, raiders]]

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

# broncos_texans_dolphins = Parlay(money_line_arr=[broncos, texans, dolphins], bet_amount=1)
# broncos_texans_dolphins.print_stats()
#
# broncos_titans_dolphins = Parlay(money_line_arr=[broncos, titans, dolphins], bet_amount=1)
# broncos_titans_dolphins.print_stats()
#
# chiefs_titans_dolphins = Parlay(money_line_arr=[chiefs, titans, dolphins], bet_amount=1)
# chiefs_titans_dolphins.print_stats()
#
# chiefs_texans_dolphins = Parlay(money_line_arr=[chiefs, texans, dolphins], bet_amount=1)
# chiefs_texans_dolphins.print_stats()
#
# chiefs_texans_giants = Parlay(money_line_arr=[chiefs, texans, giants], bet_amount=1)
# chiefs_texans_giants.print_stats()
#
# broncos_texans_giants = Parlay(money_line_arr=[broncos, texans, giants], bet_amount=1)
# broncos_texans_giants.print_stats()


binaries = [[broncos, chiefs], [texans, titans], [dolphins, giants]]

lst = list(itertools.product([0, 1], repeat=3))
print(lst)

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




def f2(num_options):
    f = np.zeros(num_options)
