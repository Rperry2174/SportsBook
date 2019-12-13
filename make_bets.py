
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

phi = MoneyLine(event="phi", bet_amount=100, odds=-115)
cle = MoneyLine(event="cle", bet_amount=100, odds=540)
det = MoneyLine(event="det", bet_amount=100, odds=260)
por = MoneyLine(event="por", bet_amount=100, odds=235)
#
bos = MoneyLine(event="bos", bet_amount=100, odds=-103)
sa = MoneyLine(event="sa", bet_amount=100, odds=-715)
dal = MoneyLine(event="dal", bet_amount=100, odds=-315)
den = MoneyLine(event="den", bet_amount=100, odds=-286)

# buf_sabres.print_stats()
# ny_rangers.print_stats()
# car_hurricanes.print_stats()
# islanders.print_stats()
# ana_ducks.print_stats()
# cgy_flames.print_stats()

binaries = [[cle, sa], [det, dal], [por, den], [phi, bos]]

x = ParlaySystem(binaries=binaries)
print("=================================================")
x.slsqp_solver()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
x.lp_solver()
print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
