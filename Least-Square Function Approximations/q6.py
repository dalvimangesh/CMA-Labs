import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from scipy.integrate import quad, romberg
from q1 import Polynomial
from q3 import getLegendrePoly
from q5 import getChebyshevPoly


def verifyChebyshevPoly(n=5):

    chebyshev = []
    epsilon = 1e-12

    for i in range(n):
        chebyshev.append(getChebyshevPoly(i))

    def w(x): return 1 / math.sqrt(1 - x**2 + epsilon)

    res = []
    a = -1
    b = 1

    for i in range(n):
        for j in range(n):
            def curFun(x): return w(x) * chebyshev[i][x] * chebyshev[j][x]
            cj = romberg( function = curFun, a=a, b=b )
            res.append([(i, j), round(cj, 2)])

    for e in res:
        print(e)


if __name__ == '__main__':

    print(verifyChebyshevPoly())
