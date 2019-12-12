from pulp import *
import pandas as pd


df = pd.DataFrame({'Variable': ['x1', 'x2'],
                   'Price': [45, 20],
                   'Cost': [30, 10],
                   'Demand': [2000, 8000]
                    })

print(df.head())

#
#
# df.eval('Margin=Price-Cost', inplace=True)
#
# # set the dictionary for each feature
# prob = LpProblem('Sell', LpMaximize) # Objective function
#
# inv_items = list(df['Variable']) # Variable name
#
# margin = dict(zip(inv_items, df['Margin'])) # Function
#
# demand = dict(zip(inv_items, df['Demand'])) # Function
#
# # next, we are defining our decision variables as investments and are adding a few parameters to it
# inv_vars = LpVariable.dicts('Vairable', inv_items, lowBound=0, cat='Integar')
#
# # set the decision variables
# # all add in the problem setting
# prob += lpSum([inv_vars[i] * margin[i] for i in inv_items])
#
# # Constraint
# prob += lpSum([inv_vars[i] for i in inv_items]) <= 8000, 'Total Demand'
#
# # Constraint
# prob += inv_vars['x1'] <= 2000, 'x1 Demand'
#
# # Constraint
# prob += inv_vars['x2'] <= 8000, 'x2 Demand'
#
# # Run this. Like click the solve to let Solver run.
# prob.solve()
#
# # Answer
# value(prob.objective) # 9000
# # Variables' values
# print('The optimal answer\n'+'-'*70)
# for v in prob.variables():
#     if v.varValue > 0:
#        print(v.name, '=', v.varValue)
