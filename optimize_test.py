# Import PuLP modeler functions
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Example_Problem", LpMinimize)

# Declare decision variables
por_over = LpVariable(name="por_over", lowBound=1, cat="Continuous")
por_under = LpVariable(name="por_under", lowBound=1, cat="Continuous")
la_over = LpVariable(name="la_over", lowBound=1, cat="Continuous")
la_under = LpVariable(name="la_under", lowBound=1, cat="Continuous")

# The objective function is added to 'prob' first
prob += (por_over*260.0/100.0+por_over) + (por_under*265.0/100.0+por_under) + (la_over*285.0/100.0+la_over) + (la_under*300.0/100.0+la_under)

# The constraints are added to 'prob'
prob += (por_over*260.0/100.0+por_over) - (por_over + por_under + la_over + la_under) >= 0
prob += (por_under*265.0/100.0+por_under) - (por_over + por_under + la_over + la_under) >= 0
prob += (la_over*285.0/100.0+la_over) - (por_over + por_under + la_over + la_under) >= 0
prob += (la_under*300.0/100.0+la_under) - (por_over + por_under + la_over + la_under) >= 0

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)
