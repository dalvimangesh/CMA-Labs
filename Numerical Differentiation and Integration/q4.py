import matplotlib.pyplot as plt
from numpy import linspace
import math


def f(x):
    return 2 * x * math.exp(x * x)


def Integral_f(x):
    return math.exp(x*x)


def show(low, high):

    numOfintervals = 100
    xPoints = []
    yPoints = []
    a, b = low, high

    originalArea = Integral_f(b) - Integral_f(a)

    for M in range(1, numOfintervals):

        area = 0
        H = (b - a) / M

        for k in range(1, M+1):
            xk = a + k * H
            xk_1 = a + (k-1) * H
            area += (f(xk) + f(xk_1))

        area = (H/2) * area
        xPoints.append(M)
        yPoints.append(area)

    plt.plot(xPoints, yPoints, color='red',label='Calculated Area at Interval M')
    plt.axhline(y=originalArea,label='Original Area')
    plt.ylabel('area')
    plt.xlabel('M')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    show(low=1, high=3)
