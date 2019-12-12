from scipy import optimize

def f(x):
    return(x[0] * 1 + x[1] * 2 + x[2] * 3 + x[3] * 4 + x[4] * 5 + x[5] * 6 + x[6] * 7 + x[7] * 8) / 8.0

ans = optimize.linprog(
    c = f,
    bounds=(1, 5),
    method='simplex'
)

print(ans)
