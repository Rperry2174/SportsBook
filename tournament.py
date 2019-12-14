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






# East region
# Note: missing 1 and 2 seeds

# duke1 =  MoneyLine(event="duke1", bet_amount=100, odds=220)
# ncccentral16 =  MoneyLine(event="ncccentral16", bet_amount=100, odds=-278)

vcu8 =  MoneyLine(event="vcu8", bet_amount=100, odds=-114)
ucf9 =  MoneyLine(event="ncccentral16", bet_amount=100, odds=-104)

virginiatech4 = MoneyLine(event="virginiatech4", bet_amount=100, odds=-530)
stlouis13 = MoneyLine(event="stlouis13", bet_amount=100, odds=410)

missst5 = MoneyLine(event="missst5", bet_amount=100, odds=-345)
liberty12 = MoneyLine(event="liberty12", bet_amount=100, odds=280)

michigan2 = MoneyLine(event="michigan2", bet_amount=100, odds=-2500)
bradley15 = MoneyLine(event="bradley15", bet_amount=100, odds=1300)

louisville7 = MoneyLine(event="louisville7", bet_amount=100, odds=-225)
minnesota10 = MoneyLine(event="minnesota10", bet_amount=100, odds=185)

lsu3 = MoneyLine(event="lsu3", bet_amount=100, odds=-335)
yale14 = MoneyLine(event="yale14", bet_amount=100, odds=275)

# maryland6 = MoneyLine(event="maryland6", bet_amount=100, odds=220)
# belmont11 = MoneyLine(event="belmont11", bet_amount=100, odds=220)

east_region_binaries = [
    [vcu8, ucf9],
    [virginiatech4, stlouis13],
    [missst5,liberty12],
    [michigan2, bradley15],
    [louisville7, minnesota10],
    [lsu3, yale14],
]



# syracuse8 = MoneyLine(event="syracuse8", bet_amount=100, odds=220)
# baylor9 = MoneyLine(event="baylor9", bet_amount=100, odds=220)
#
# floridastate4 = MoneyLine(event="floridastate4", bet_amount=100, odds=220)
# vermont13 = MoneyLine(event="vermont13", bet_amount=100, odds=220)
#
# marquette5 = MoneyLine(event="marquette5", bet_amount=100, odds=220)
# murrayst12 = MoneyLine(event="murrayst12", bet_amount=100, odds=220)
#
# michigan2 = MoneyLine(event="michigan2", bet_amount=100, odds=220)
# montana15 = MoneyLine(event="montana15", bet_amount=100, odds=220)
#
# nevada7 = MoneyLine(event="nevada7", bet_amount=100, odds=220)
# florida10 = MoneyLine(event="florida10", bet_amount=100, odds=220)
#
# texastech3 = MoneyLine(event="texastech3", bet_amount=100, odds=220)
# nkentucky14 = MoneyLine(event="nkentucky14", bet_amount=100, odds=220)
#
# buffalo6 = MoneyLine(event="buffalo6", bet_amount=100, odds=220)
# arizonast11 = MoneyLine(event="arizonast11", bet_amount=100, odds=220)


# binaries = [
#     [virginiatech4, stlouis13],
#     [michigan2, bradley15
#     [louisville7, minnesota10],
#     [lsu3, yale14],
#     [maryland6, belmont11],
#     [nebraska, indiana],
#     [colorado, cstate],
#     [pover, punder],
#     [prarieview, loyola],
#     [gkminus1, dalstarsplus1],
# ]

# binaries = east_region_binaries

TOURNEY_SIZE = len(east_region_binaries)
SELECT_NUM = 3

def findsubsets(s, n):
    return list(itertools.combinations(s, n))

s = set()
n = SELECT_NUM

for i in range(TOURNEY_SIZE):
    s.add(i)

all_subsets = findsubsets(s, n)
csv = []
df = pd.DataFrame()
# print(all_subsets)
# print(len(all_subsets))


for i in range(len(all_subsets)):
    current_subset = all_subsets[i]
    parlay_binaries = []
    for i in range(len(current_subset)):
        index = current_subset[i]
        parlay_binaries.append(east_region_binaries[index])

    ps = ParlaySystem(binaries=parlay_binaries,
                    target_profit=1.2,
                    bounds=(0.01, 30),
                    binary_index_arr=list(current_subset)
                    )
    csv_res, raw_df = ps.slsqp_solver()
    df = pd.concat([df, raw_df])
    csv.append(tmp_res)

print(csv)
print(ps.create_ml_dict())
