import matplotlib.pyplot as plt
from numpy import linspace
import math


def sinx2(x):
    return math.sin(x*x)


def d_sinx2(x):
    return math.cos(x*x) * 2 * x

# forward finite difference approximation
def ffd(f, x, h):
    nR = f(x+h) - f(x)
    dR = h
    return nR / dR


def bfd(f, x, h):
    nR = f(x) - f(x-h)
    dR = h
    return nR / dR


def cfd(f, x, h):
    nR = f(x+h) - f(x-h)
    dR = 2*h
    return nR / dR


def show(low, high):

    xPoints = linspace(low, high, 250)

    y1Points = [ abs(d_sinx2(num) - ffd(f=sinx2, x=num, h=0.01)) for num in xPoints ]

    y2Points = [ abs(d_sinx2(num) - bfd(f=sinx2, x=num, h=0.01)) for num in xPoints ]

    y3Points = [ abs(d_sinx2(num) - cfd(f=sinx2, x=num, h=0.01)) for num in xPoints]

    plt.plot(xPoints, y1Points, color='green', label="| f'(x) - δ⁺(x)|")
    plt.plot(xPoints, y2Points, color='blue', label="| f'(x) - δ⁻(x)|")
    plt.plot(xPoints, y3Points, color='red',label="| f'(x) - δᶜ(x)|")
    plt.title('absolute errors of approximationof \nδ⁺(x), δ⁻(x) and δᶜ(x) of sin(x^2)')
    plt.xlabel('x')
    plt.ylabel('Absolute error')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':

    show(low=0, high=1)
