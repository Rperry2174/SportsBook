
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

jazz = MoneyLine(event="jazz", bet_amount=100, odds=-1430)
gs_warriors = MoneyLine(event="gs_warriors", bet_amount=100, odds=900)

army = MoneyLine(event="army", bet_amount=100, odds=325)
navy = MoneyLine(event="navy", bet_amount=100, odds=-435)



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
# binaries = [[por, den], [moreno, france], [iowa, iowa_st]]
# binaries = [[por, den], [jazz, gs_warriors], [iowa, iowa_st]]

# binaries = [[por, den], [northern_iowa, grand_canyon], [iowa, iowa_st]] # best
binaries = [[por, den], [northern_iowa, grand_canyon], [army, navy], [iowa, iowa_st]]


# devils = MoneyLine(event="devils", bet_amount=100, odds=-200)
# coyotes = MoneyLine(event="coyotes", bet_amount=100, odds=160)
#
# red_wings = MoneyLine(event="red_wings", bet_amount=100, odds=360)
# canadiens = MoneyLine(event="canadiens", bet_amount=100, odds=-500)
#
# kings = MoneyLine(event="kings", bet_amount=100, odds=185)
# penguins = MoneyLine(event="penguins", bet_amount=100, odds=-230)
#
# binaries = [[devils, coyotes], [red_wings, canadiens], [kings, penguins]]

# NOTE: 0 - POSITIVE_NUMBER + NEGATIVE_NUMBER (Maximize that)

# vgs = MoneyLine(event="vgs", bet_amount=100, odds=120)
# dal = MoneyLine(event="dal", bet_amount=100, odds=-139)
#
# nj = MoneyLine(event="nj", bet_amount=100, odds=550)
# col = MoneyLine(event="col", bet_amount=100, odds=-835)
#
# ov5 = MoneyLine(event="ov5", bet_amount=100, odds=140)
# un5 = MoneyLine(event="un5", bet_amount=100, odds=-175)
#
# njov5 = MoneyLine(event="njov5", bet_amount=100, odds=-375)
# njun5 = MoneyLine(event="njun5", bet_amount=100, odds=280)
#
# binaries = [[nj, col], [ov5, un5], [njov5, njun5]]


pacers = MoneyLine(event="pacers", bet_amount=100, odds=-250)
hawks = MoneyLine(event="hawks", bet_amount=100, odds=205)

hornets = MoneyLine(event="hornets", bet_amount=100, odds=215)
bulls = MoneyLine(event="bulls", bet_amount=100, odds=-265)

warriors = MoneyLine(event="warriors", bet_amount=100, odds=750)
jazz = MoneyLine(event="jazz", bet_amount=100, odds=-1115)

knicks = MoneyLine(event="knicks", bet_amount=100, odds=270)
kings = MoneyLine(event="kings", bet_amount=100, odds=-335)

nebraska  = MoneyLine(event="nebraska", bet_amount=100, odds=1000)
indiana  = MoneyLine(event="indiana", bet_amount=100, odds=-2000)

gardnerwebb  = MoneyLine(event="gardnerwebb", bet_amount=100, odds=-480)
kennesaw  = MoneyLine(event="kennesaw", bet_amount=100, odds=360)

pover  = MoneyLine(event="pover", bet_amount=100, odds=135)
punder  = MoneyLine(event="punder", bet_amount=100, odds=-186)

hover  = MoneyLine(event="hover", bet_amount=100, odds=460)
hunder  = MoneyLine(event="hunder", bet_amount=100, odds=460)

colorado  = MoneyLine(event="colorado", bet_amount=100, odds=-205)
cstate  = MoneyLine(event="cstate", bet_amount=100, odds=165)

prarieview  = MoneyLine(event="prarieview", bet_amount=100, odds=255)
loyola  = MoneyLine(event="loyola", bet_amount=100, odds=-335)

gkminus1 =  MoneyLine(event="gkminus1", bet_amount=100, odds=220)
dalstarsplus1 =  MoneyLine(event="dalstarsplus1", bet_amount=100, odds=-278)

binaries = [
    [pacers, hawks],
    # [hornets, bulls],
    # [warriors, jazz],
    # [knicks, kings],
    [gardnerwebb, kennesaw],
    # [nebraska, indiana],
    # [colorado, cstate],
    # [pover, punder],
    # [prarieview, loyola],
    [gkminus1, dalstarsplus1],
]

# Best so far
# binaries = [
#     [gardnerwebb, kennesaw],
#     [nebraska, indiana],
#     [prarieview, loyola],
# ]

x = ParlaySystem(binaries=binaries, target_profit=1.2, bounds=(0.01, 30))
print("=================================================")
x.slsqp_solver()
#
#                                         event   bet  multiplier  payout  profit
# 4    gardnerwebb_indiana_colorado_prarieview_  0.08    6.701166  0.5138   -0.00
# 5        gardnerwebb_indiana_colorado_loyola_  0.01    2.451131  0.0245   -0.49
# 7          gardnerwebb_indiana_cstate_loyola_  0.03    4.365826  0.1459   -0.37


# Darts
# huybrechts = MoneyLine(event="huybrechts", bet_amount=100, odds=-286)
# nentjes = MoneyLine(event="nentjes", bet_amount=100, odds=220)
#
# humphries = MoneyLine(event="humphries", bet_amount=100, odds=-167)
# petersen = MoneyLine(event="petersen", bet_amount=100, odds=133)
#
# labanauskas = MoneyLine(event="labanauskas", bet_amount=100, odds=-190)
# edgar = MoneyLine(event="edgar", bet_amount=100, odds=150)
#
# meikle = MoneyLine(event="meikle", bet_amount=100, odds=-335)
# yamada = MoneyLine(event="yamada", bet_amount=100, odds=250)
#
#
# binaries = [[huybrechts, nentjes], [labanauskas, edgar], [meikle, yamada]]
#
# x = ParlaySystem(binaries=binaries, target_profit=0.5, bounds=(0.01, 30))
# print("=================================================")
# x.slsqp_solver()
