from classes import *

assert sum([1, 2, 3]) == 6, "Should be 6"

bulls = MoneyLine(event="bulls", bet_amount=100, odds=200)
mavericks = MoneyLine(event="mavericks", bet_amount=100, odds=525)
rockets = MoneyLine(event="rockets", bet_amount=100, odds=-560)

bulls.set_index(0)
mavericks.set_index(1)
rockets.set_index(2)

assert bulls.odds == 200, "should be 200"
assert bulls.multiplier == 3, "should be 3"
assert bulls.payout == 300.0, "should be 300.0"

two_team_parlay = Parlay(
    money_line_arr=[bulls, mavericks],
    bet_amount=100)

assert two_team_parlay.odds == 1775.0, "should be 1775.0"
assert two_team_parlay.multiplier == 18.75, "should be 18.75"
assert two_team_parlay.payout == 1875.0, "should be 1875.0"

three_team_parlay = Parlay(
    money_line_arr=[bulls, mavericks, rockets],
    bet_amount=100)

assert round(three_team_parlay.odds, 2) == 2109.82, "should be 2109.82"
assert round(three_team_parlay.multiplier, 2) == 22.10, "should be 22.10"
assert round(three_team_parlay.payout, 2) == 2209.82, "should be 2209.82"

three_team_parlay.override_odds(200)
assert three_team_parlay.odds == 200, "should be 200"
assert three_team_parlay.multiplier == 3, "should be 3"
assert three_team_parlay.payout == 300.0, "should be 300.0"

print(three_team_parlay.index_arr)
