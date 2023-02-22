import matplotlib.pyplot as plt
from numpy import linspace
from scipy.integrate import quad,romberg, trapezoid,simpson
import math

# given function
def f(x):
    return 2 * x * math.exp(x * x)

# integration of given function
def Integral_f(x):
    return math.exp(x*x)

def show(low, high):

    '''
    Function to visualize, as a function of u, area under the curve y(x) = 2*x*exp(x²) in the
    interval [0, u] computed using various integration functions available in Pythons scipy.integrate
    module.
    '''

    xPoints = linspace(low,high,1000) # x points
    originalArea = [] # to store original area using definite integration
    quadArea = [] # to store area using quad
    rombergArea = [] # to store area using romberg
    trapezoidArea = [] # to store area using trapezoid 
    simpsonArea = [] # to store area usng simposon 

    for u in xPoints: # to each u

        curXPoints = linspace(low,u,100)

        curYPoints = [ f(x) for x in curXPoints ]

        originalArea.append( Integral_f(u) - Integral_f(low) ) # original area

        quadArea.append( quad( func = f , a=low, b = u )[0] ) # area using quad
        
        rombergArea.append( romberg( function = f, a=low, b = u ) ) # area using romberg

        trapezoidArea.append( trapezoid(x = curXPoints,  y = curYPoints ) ) # area using romberg

        simpsonArea.append ( simpson( x = curXPoints, y = curYPoints ) ) # area using simpson

    # ploting the results
    plt.plot(xPoints,originalArea,color='red',linestyle='dashed',label='original',dashes=(5, 2),linewidth=1.8)
    plt.plot(xPoints,quadArea,color='orange',linestyle='dashed',label='quad',dashes=(5, 3),linewidth=1.8)
    plt.plot(xPoints,simpsonArea,color='yellow',linestyle='dashed',label='romberg',dashes=(5, 5),linewidth=1.8)
    plt.plot(xPoints,rombergArea,color='green',linestyle='dashed',label='trapzoid',dashes=(5, 8),linewidth=1.8)
    plt.plot(xPoints,trapezoidArea,color='blue',linestyle='dashed',label='simpson',dashes=(5, 11),linewidth=1.8)
    plt.title('area under the curve using various integration functions')
    plt.xlabel('u')
    plt.ylabel('area')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    show(low=0, high=1)
