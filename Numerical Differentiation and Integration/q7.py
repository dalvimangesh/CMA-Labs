from q6 import Polynomial
import math
from numpy import linspace
from random import randint

def f(x):
    return math.exp(x) * math.sin(x)

def showArea(low,high):

    xPoints = linspace( 0 , 10 , 100)
    points = [ (x,f(x)) for x in xPoints ]

    p = Polynomial([])
    p = p.fitViaMatrixMethod( points = points , isPlot = False)

    calArea = p.area(0,10, isString=False)

    actualArea = 0.171775

    print( "Calculated Area : ", calArea)
    print( "Error ( Actual - Calculated ) : " , actualArea - calArea )


if __name__=='__main__':

    showArea(0,0.5)