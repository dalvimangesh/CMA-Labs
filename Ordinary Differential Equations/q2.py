import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from q1 import Polynomial


def forwardEulerMethod(ode, originalSol, hlist, x0=5, a=0, b=10):
    '''
    Function that uses the backward Euler method to solve the ODE x (t) = -2x(t), with
    initial condition x(0) = 5, in the interval [0, 10], computes a polynomial that passes through
    the discrete solution points of the ODE.
    '''

    # Loop through each step size in the list of h values
    for h in hlist:

        xPoints = [x0]
        points = [(0, x0)]
        tPoints = list(np.arange(a, b, h))

        # Perform the backward Euler method
        for i in range(1, len(tPoints)):

            # Update x using the Euler backward method
            xPoints.append(ode(tPoints[i-1], xPoints[i-1], h))
            points.append((tPoints[i], xPoints[i]))

        p = Polynomial([0])
        p.fitViaMatrixMethod(points=points)

    # Result
    xPoints = list(np.linspace(a, b, 100))
    yPoints = list(map(originalSol, xPoints))
    print(yPoints)
    plt.plot(xPoints, yPoints, color='red')
    plt.ylim(-6, 6)
    plt.show()


if __name__ == '__main__':

    def givenODE(t, x, h): return (x / (1 + 2*h))

    def originalSol(x): return math.exp(-2*x) * 5

    hlist = [0.1, 0.5, 1, 2, 3]

    forwardEulerMethod(ode=givenODE, originalSol=originalSol, hlist=hlist)
