# Python Program to Print
# all subsets of given size of a set

import itertools
from parlay_system import *

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
    [hornets, bulls],
    [warriors, jazz],
    [knicks, kings],
    [gardnerwebb, kennesaw],
    [nebraska, indiana],
    [colorado, cstate],
    [pover, punder],
    [prarieview, loyola],
    [gkminus1, dalstarsplus1],
]

TOURNEY_SIZE = len(binaries)
SELECT_NUM = 3

def findsubsets(s, n):
    return list(itertools.combinations(s, n))

s = set()
n = SELECT_NUM

for i in range(TOURNEY_SIZE):
    s.add(i)

all_subsets = findsubsets(s, n)
csv = []
# print(all_subsets)
# print(len(all_subsets))


for i in range(len(all_subsets)):
    current_subset = all_subsets[i]
    parlay_binaries = []
    for i in range(len(current_subset)):
        index = current_subset[i]
        parlay_binaries.append(binaries[index])

    ps = ParlaySystem(binaries=parlay_binaries,
                    target_profit=1.2,
                    bounds=(0.01, 30),
                    index_arr=list(current_subset)
                    )
    tmp_res = ps.slsqp_solver()
    csv.append(tmp_res)

print(csv)
