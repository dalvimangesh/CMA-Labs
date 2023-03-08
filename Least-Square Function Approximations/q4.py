import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from scipy.integrate import romberg
from q1 import Polynomial
from q3 import getLegendrePoly


def bestFitUsingLegendrePoly(n):

    legPoly = []

    for i in range(n+1):
        legPoly.append(getLegendrePoly(i))

    def f(x): return math.exp(x)
    def w(_): return 1

    a = []

    for j in range(n+1):

        def curFun(x): return w(x) * legPoly[j][x] * legPoly[j][x]
        cj = romberg(function=curFun, a=-1, b=1)

        def curFun(x): return w(x) * legPoly[j][x] * f(x)
        aj = (1/cj) * (romberg(function=curFun, a=-1, b=1))

        a.append(aj)

    p = Polynomial([0])

    for i in range(n+1):
        p = p + a[i] * legPoly[i]

    p.show(low=-1, high=1, toShow=False)

    xPoints = list(np.linspace(-1, 1, 100))
    yPoints = list(map(f, xPoints))

    plt.plot(xPoints, yPoints, color='red',dashes=(5,3),linewidth=2.2)

    plt.show()


if __name__ == '__main__':

    bestFitUsingLegendrePoly(n=5)