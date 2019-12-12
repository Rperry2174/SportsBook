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

# ml = MoneyLine(event="broncos", bet_amount=10, odds=120)
# ml.print_stats()
#
# ml = MoneyLine(event="broncos", bet_amount=15, odds=-150)
# ml.print_stats()
