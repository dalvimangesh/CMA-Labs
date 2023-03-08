import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import romberg
from q1 import Polynomial
from q3 import getLegendrePoly

def bestFitUsingLegendrePoly(n):

    '''
    function to compute the least-square approximation of e^x in the interval [-1,1] using
    the first n Legendre polynomials.
    '''

    try:
        if n < 0: raise Exception('n should be non negative')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)

    legPoly = []

    for i in range(n+1):
        legPoly.append(getLegendrePoly(i))

    # define the function f(x) and the weight function w(x)
    def f(x): return math.exp(x)
    def w(_): return 1

    a = []

    for j in range(n+1):

        def curFun(x): return w(x) * legPoly[j][x] * legPoly[j][x]
        cj = romberg(function=curFun, a=-1, b=1)

        # compute the coefficients aj using the Legendre polynomials
        def curFun(x): return w(x) * legPoly[j][x] * f(x)
        aj = (1/cj) * (romberg(function=curFun, a=-1, b=1))

        a.append(aj)

    # compute the polynomial of degree n that is the best fit for f(x)
    p = Polynomial([0])

    for i in range(n+1):
        p = p + a[i] * legPoly[i]

    # Result
    p.show(low=-1, high=1, toShow=False)
    xPoints = list(np.linspace(-1, 1, 100))
    yPoints = list(map(f, xPoints))
    plt.plot(xPoints, yPoints, color='red',dashes=(5,3),linewidth=2.2,label='eˣ')
    plt.title("Best fit polynomial")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.legend()
    plt.show()


if __name__ == '__main__':

    bestFitUsingLegendrePoly(n=5)