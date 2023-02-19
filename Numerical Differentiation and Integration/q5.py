import matplotlib.pyplot as plt
from numpy import linspace
from scipy.integrate import quad,romberg, trapezoid,simpson
import math

def f(x):
    return 2 * x * math.exp(x * x)

def Integral_f(x):
    return math.exp(x*x)

def show(low, high):

    xPoints = linspace(low,high,1000)
    originalArea = []
    quadArea = []
    rombergArea = []
    trapezoidArea = []
    simpsonArea = []

    for u in xPoints:

        curXPoints = linspace(low,u,100)
        curYPoints = [ f(x) for x in curXPoints ]

        originalArea.append( Integral_f(u) - Integral_f(low) )
        quadArea.append( quad( func = f , a=low, b = u )[0] )
        rombergArea.append( romberg( function = f, a=low, b = u ) )
        trapezoidArea.append( trapezoid(x = curXPoints,  y = curYPoints ) )
        simpsonArea.append ( simpson( x = curXPoints, y = curYPoints ) )

    plt.plot(xPoints,originalArea,color='red',linestyle='solid',label='original')
    plt.plot(xPoints,quadArea,color='orange',linestyle='solid',label='quad')
    plt.plot(xPoints,simpsonArea,color='yellow',linestyle='solid',label='romberg')
    plt.plot(xPoints,rombergArea,color='green',linestyle='solid',label='trapzoid')
    plt.plot(xPoints,trapezoidArea,color='blue',linestyle='solid',label='simpson')
    plt.title('area under the curve using various integration functions')
    plt.xlabel('u')
    plt.ylabel('area')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    show(low=0, high=1)
