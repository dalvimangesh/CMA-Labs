import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from scipy.integrate import romberg, quad
from q1 import Polynomial
from q3 import getLegendrePoly
from q5 import getChebyshevPoly


def fourierApproximation(n=10):

    a = -math.pi
    b = math.pi
    A,B = [],[]

    f = lambda x : math.exp(x)

    for k in range(0,n+1):

        curFun = lambda x : f(x) * math.cos(k*x)
        A.append((1/math.pi)*quad(func=curFun,a=a,b=b)[0])

        curFun = lambda x : f(x)*math.sin(k*x)
        B.append((1/math.pi)*quad(func=curFun,a=a,b=b)[0])

    xPoints = list(np.linspace(a,b,100))
    y1Points = list(map(f,xPoints))
    y2Points = []

    for x in xPoints:
        sum1, sum2 = 0,0

        for k in range(1,n+1):
            sum1 += A[k] * math.cos(k*x)
            sum2 += B[k] * math.sin(k*x)
        
        S = (A[0]/2) + sum1 + sum2
        y2Points.append(S)

    plt.plot(xPoints,y1Points)
    plt.plot(xPoints,y2Points)
    plt.show()

if __name__ == '__main__':

    print(fourierApproximation())
