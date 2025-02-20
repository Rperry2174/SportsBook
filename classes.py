import math
import itertools
import numpy as np
import pandas as pd

class MoneyLine():
    def __init__(self, event, bet_amount, odds):
        self.index = None
        self.event = event
        self.bet_amount = bet_amount
        self.odds = odds
        self.multiplier = self.odds_to_multiplier()
        self.payout = self.multiplier_to_payout()
        self.statistics = self.update_statistics()

    def set_index(self, new_index):
        self.index = new_index

    def odds_to_multiplier(self):
        if self.odds > 0:
            return 1 + (self.odds / 100.0)
        else:
            return 1 + (100.0 / abs(self.odds))

    def multiplier_to_payout(self):
        return self.multiplier * self.bet_amount

    def update_statistics(self):
        return pd.DataFrame({
            'event': [self.event],
            'bet_amount': [self.bet_amount],
            'odds': [self.odds],
            'multiplier': [self.multiplier],
            'payout': [self.payout]
        })

    def print_stats(self):
        df = pd.DataFrame({'event': [self.event],
                           'bet_amount': [self.bet_amount],
                           'odds': [self.odds],
                           'multiplier': [self.multiplier],
                           'payout': [self.payout]
                           })
        print(df)

class Parlay():
    def __init__(self, money_line_arr, bet_amount):
        self.money_line_arr = money_line_arr
        self.event = self.format_events()
        self.index_arr = self.create_index_arr()
        self.bet_amount = bet_amount

        self.multiplier = self.ml_arr_to_multiplier()
        self.payout = self.multiplier_to_payout()
        self.odds = self.payout_to_odds()
        self.statistics = self.update_statistics()

    def update_bet_amount(self, new_bet_amount):
        self.bet_amount = new_bet_amount
        self.payout = self.multiplier_to_payout()
        self.odds = self.payout_to_odds()
        self.statistics = self.update_statistics()

    def ml_arr_to_multiplier(self):
        parlay_multiplier = 1
        for ml in self.money_line_arr:
            parlay_multiplier *= ml.multiplier

        return parlay_multiplier

    def multiplier_to_payout(self):
        return self.multiplier * self.bet_amount

    def payout_to_odds(self):
        return 100.0 * ((self.payout / self.bet_amount) - 1.0)

    def odds_to_multiplier(self):
        if self.odds > 0:
            return 1 + (self.odds / 100.0)
        else:
            return 1 + (100.0 / abs(self.odds))

    def override_odds(self, new_odds):
        self.odds = new_odds
        self.multiplier = self.odds_to_multiplier()
        self.payout = self.multiplier_to_payout()

    def create_index_arr(self):
        result = []
        for ml in self.money_line_arr:
            result.append(ml.index)

        return result

    def update_statistics(self):
        return pd.DataFrame({
            'event': [self.event],
            'bet_amount': [self.bet_amount],
            'odds': [self.odds],
            'multiplier': [self.multiplier],
            'payout': [self.payout]
        })

    def format_events(self):
        result = ""
        for ml in self.money_line_arr:
            result += ml.event + "_"

        return result[:-1]

    def format_stats_for_csv(self):
        items = [self.event, str(self.bet_amount), str(self.odds), str(self.payout)]
        return ",".join(items)

    def print_stats(self):
        df = pd.DataFrame({'event': [self.event],
                           'bet_amount': [self.bet_amount],
                           'odds': [self.odds],
                           'multiplier': [self.multiplier],
                           'payout': [self.payout]
                           })
        print(df)

# ml = MoneyLine(event="broncos", bet_amount=10, odds=120)
# ml.print_stats()
#
# ml = MoneyLine(event="broncos", bet_amount=15, odds=-150)
# ml.print_stats()
#
# bears = MoneyLine(event="bears", bet_amount=15, odds=425)
# broncos = MoneyLine(event="broncos", bet_amount=15, odds=190)
#
# p = Parlay(money_line_arr=[bears, broncos], bet_amount=1)
# p.print_stats()
