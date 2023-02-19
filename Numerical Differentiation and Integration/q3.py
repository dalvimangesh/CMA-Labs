import matplotlib.pyplot as plt
from numpy import linspace
import math


def sinx2(x):
    return math.sin(x*x)

def d_sinx2(x):
    return math.cos(x*x) * 2 * x

def dd_sinx2(x):
    return 2 * (math.cos(x * x) - 2 * x * x * math.sin(x * x))

def ddd_sinx2(x):
    return -4 * x * (3 * math.sin(x * x) + 2 * x * x * math.cos(x * x))

# forward finite difference approximation
def ffd(f, x, h):
    nR = f(x+h) - f(x)
    dR = h
    return nR / dR

# backward finite difference approximation
def bfd(f, x, h):
    nR = f(x) - f(x-h)
    dR = h
    return nR / dR

# centered finite difference approximation
def cfd(f, x, h):
    nR = f(x+h) - f(x-h)
    dR = 2*h
    return nR / dR


def show(low, high):

    hPoints = linspace(low, high, 100)
    hPoints = hPoints[1:]
    ffdCalculated = []
    ffdTheoretical = []

    cfdCalculated = []
    cfdTheoretical = []

    for h in hPoints:

        if h == 0:
            continue

        ffdCalCurMax, cfdCalCurMax = 0, 0
        ffdTheoryCurMax, cfdTheoryCurMax = 0, 0

        for x in linspace(low, high, 100):

            ffdCalCurMax = max(ffdCalCurMax, abs( ffd(f=sinx2, x=x, h=h) - d_sinx2(x)))
            cfdCalCurMax = max(cfdCalCurMax, abs( cfd(f=sinx2, x=x, h=h) - d_sinx2(x)))

            for i in linspace(x, x+h, 100):

                ffdTheoryCurMax = max(ffdTheoryCurMax, abs((h/2) * dd_sinx2(i)))
                cfdTheoryCurMax = max(cfdTheoryCurMax, abs((h*h/6) * ddd_sinx2(i)))

        ffdCalculated.append(ffdCalCurMax)
        ffdTheoretical.append(ffdTheoryCurMax)

        cfdCalculated.append(cfdCalCurMax)
        cfdTheoretical.append(cfdTheoryCurMax)

    plt.plot(hPoints,ffdCalculated,color='red',label='Forward Approx')
    plt.plot(hPoints,ffdTheoretical,color='blue',label='Theoretical forward Approx')
    plt.plot(hPoints,cfdCalculated,color='orange',label='Centered Approx')
    plt.plot(hPoints,cfdTheoretical,color='green',label='Theoretical Centered Approx')
    plt.xlabel('h')
    plt.ylabel('Maximum absolute error')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':

    show(low=0, high=1)