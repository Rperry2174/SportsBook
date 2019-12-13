
from parlay_system import *

# # Create the 'prob' variable to contain the problem data
#
# broncos = MoneyLine(event="broncos", bet_amount=100, odds=440)
# texans = MoneyLine(event="texans", bet_amount=100, odds=128)
# dolphins = MoneyLine(event="dolphins", bet_amount=100, odds=148)
# #
# chiefs = MoneyLine(event="chiefs", bet_amount=100, odds=-560)
# titans = MoneyLine(event="titans", bet_amount=100, odds=-157)
# giants = MoneyLine(event="giants", bet_amount=100, odds=-182)
#
# broncos.print_stats()
# texans.print_stats()
# dolphins.print_stats()
# #
# chiefs.print_stats()
# titans.print_stats()
# giants.print_stats()
#
#
# binaries = [[broncos, chiefs], [texans, titans], [dolphins, giants]]
# x = ParlaySystem(binaries=binaries)
# print("=================================================")
# x.slsqp_solver()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
# x.lp_solver()
# print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
#



# buf_sabres = MoneyLine(event="buf_sabres", bet_amount=100, odds=145)
# ny_rangers = MoneyLine(event="ny_rangers", bet_amount=100, odds=118)
# car_hurricanes = MoneyLine(event="car_hurricanes", bet_amount=100, odds=106)
# #
# islanders = MoneyLine(event="islanders", bet_amount=100, odds=-180)
# ana_ducks = MoneyLine(event="ana_ducks", bet_amount=100, odds=-143)
# cgy_flames = MoneyLine(event="cgy_flames", bet_amount=100, odds=-129)
#
# buf_sabres.print_stats()
# ny_rangers.print_stats()
# car_hurricanes.print_stats()
# islanders.print_stats()
# ana_ducks.print_stats()
# cgy_flames.print_stats()
#
# binaries = [[buf_sabres, islanders], [ny_rangers, ana_ducks], [car_hurricanes, cgy_flames]]
#
# x = ParlaySystem(binaries=binaries)
# print("=================================================")
# x.slsqp_solver()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
# x.lp_solver()
# print("|||||||||||||||||||||||||||||||||||||||||||||||||||")

phi = MoneyLine(event="phi", bet_amount=100, odds=-110)
bos = MoneyLine(event="bos", bet_amount=100, odds=-108)

cle = MoneyLine(event="cle", bet_amount=100, odds=540)
sa = MoneyLine(event="sa", bet_amount=100, odds=-715)

dal = MoneyLine(event="dal", bet_amount=100, odds=-315)
det = MoneyLine(event="det", bet_amount=100, odds=260)

por = MoneyLine(event="por", bet_amount=100, odds=235)
den = MoneyLine(event="den", bet_amount=100, odds=-286)

iowa = MoneyLine(event="iowa", bet_amount=100, odds=148)
iowa_st = MoneyLine(event="iowa_st", bet_amount=100, odds=-180)

northern_iowa = MoneyLine(event="northern_iowa", bet_amount=100, odds=-250)
grand_canyon = MoneyLine(event="grand_canyon", bet_amount=100, odds=205)

moreno = MoneyLine(event="moreno", bet_amount=100, odds=-167)
france = MoneyLine(event="france", bet_amount=100, odds=135)
# buf_sabres.print_stats()
# ny_rangers.print_stats()
# car_hurricanes.print_stats()
# islanders.print_stats()
# ana_ducks.print_stats()
# cgy_flames.print_stats()

# binaries = [[cle, sa], [det, dal], [por, den], [phi, bos]]
# binaries = [[det, dal], [por, den], [phi, bos], [iowa, iowa_st]] # 2nd best
# binaries = [[det, dal], [por, den], [northern_iowa, grand_canyon], [iowa, iowa_st], [phi, bos]]
# binaries = [[det, dal], [por, den], [northern_iowa, grand_canyon], [iowa, iowa_st]]
# binaries = [[test1, test2], [por, den], [northern_iowa, grand_canyon], [iowa, iowa_st]]
binaries = [[por, den], [moreno, france], [iowa, iowa_st]]
# binaries = [[por, den], [northern_iowa, grand_canyon], [iowa, iowa_st]] # best




# NOTE: 0 - POSITIVE_NUMBER + NEGATIVE_NUMBER (Maximize that)
x = ParlaySystem(binaries=binaries, target_profit=0.5, bounds=(0.01, 30))
print("=================================================")
x.slsqp_solver()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
# x.lp_solver()
# print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
