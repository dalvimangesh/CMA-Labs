import matplotlib.pyplot as plt
from numpy import linspace
import math

def sinx2(x):
    return math.sin(x*x)

def d_sinx2(x):
    return math.cos(x*x) * 2 * x

# forward finite difference approximation
def ffd(f,x,h):
    nR = f(x+h) - f(x)
    dR = h
    return nR / dR

def show(low,high):

    xPoints = linspace(low,high,250)
    y1Points = list( map( d_sinx2, xPoints ) )
    y2Points = list( map( lambda x : ffd(f = sinx2, x = x, h = 0.01) , xPoints) )

    plt.plot(xPoints,y1Points,'r',label='actual derivative',linestyle='solid',linewidth='1.5')
    plt.plot(xPoints,y2Points,'b:',label='forward finite difference approximation',linewidth='2.5')
    plt.title('visualize of the function sin(x^2)')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    show(low=0,high=1)