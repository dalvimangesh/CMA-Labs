from q6 import Polynomial
import math
from numpy import linspace
from random import randint

# given function
def f(x):
    return math.exp(x) * math.sin(x)

def showArea(low,high):

    '''
    Using fitmatrix method of the polynomial class to create the
    polynomial form of the given function by generating (x,f(x))
    points and calculating area of the same in given range using 
    method area of polynomial class
    '''

    xPoints = linspace( -10 , 10 , 100)
    points = [ (x,f(x)) for x in xPoints ]

    p = Polynomial([])
    p = p.fitViaMatrixMethod( points = points , isPlot = False)

    calArea = p.area(0,0.5, isString=False)

    actualArea = 0.171775 # Actual area

    print( "Calculated Area : ", calArea)
    print( "Error ( Actual - Calculated ) : " , actualArea - calArea )


if __name__=='__main__':

    showArea(0,0.5)