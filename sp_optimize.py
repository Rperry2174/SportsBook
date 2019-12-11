import scipy.optimize as optimize
import numpy as np
import numpy.matlib as mb
import statistics

testArr = [2, -1]

def f(x):   # The rosenbrock function

    por_over = x[0]
    por_under = x[1]
    la_over = x[2]
    la_under = x[3]

    # return .5*(1 - x[0])**2 + (x[1] - x[0]**2)**2
    return -statistics.mean([(por_over*260.0/100.0+por_over), (por_under*265.0/100.0+por_under), (la_over*285.0/100.0+la_over), (la_under*400.0/100.0+la_under)])

# def ConsSSLn(x):
#     return np.sum(x,axis=1)

# cons=({'type':'ineq','fun':ConsSSLn})

bnds = ((1, None), (1, None), (1, None), (1, None))
cons = ({'type': 'ineq', 'fun': lambda x: x[0]*260.0/100.0+x[0] - (x[0] + x[1] + x[2] + x[3]) },
        {'type': 'ineq', 'fun': lambda x: x[1]*265.0/100.0+x[1] - (x[0] + x[1] + x[2] + x[3]) },
        {'type': 'ineq', 'fun': lambda x: x[2]*285.0/100.0+x[2] - (x[0] + x[1] + x[2] + x[3]) },
        {'type': 'ineq', 'fun': lambda x: x[3]*400.0/100.0+x[3] - (x[0] + x[1] + x[2] + x[3]) })

FinalVal= optimize.minimize(f, [2, -1, -4, 5], method="SLSQP", bounds=bnds, constraints=cons)
print(FinalVal)
 #     fun: -4.946519419005897
 #     jac: array([-0.89999998, -0.91249996, -0.96249998, -1.25      ])
 # message: 'Positive directional derivative for linesearch'
 #    nfev: 147
 #     nit: 18
 #    njev: 14
 #  status: 8
 # success: False
 #       x: array([1.38019284, 1.34437056, 1.27543659, 1.        ])


 FinalVal= optimize.minimize(f, [2, -1, -4, 5], method="SLSQP", bounds=bnds, constraints=cons)
 print(FinalVal)
