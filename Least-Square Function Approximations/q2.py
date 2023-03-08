import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import romberg
from q1 import Polynomial

def bestFitFunction(f,n,a = 0,b = math.pi) -> None:

    '''
    function to compute the polynomial of degree n that best approximates the function
    sin(x) + cos(x) in the interval [0, π].
    '''
    
    try:
        if n < 0: raise Exception('n should be non negative')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)

    A = []
    B = []

    # finding A matrix by computing the romberg integration
    for j in range(0,n+1):
        curRow = []
        for k in range(0,n+1):
            curFun = lambda x : x**(j+k)
            curRow.append(romberg(function=curFun,a=a,b=b))
        A.append(curRow)

    # Populate B matrix by computing the Romberg integration over the interval [a, b]
    for j in range(0,n+1):
        curFun = lambda x : (x**j) * f(x)
        B.append(romberg(function=curFun,a=a,b=b))

    # Solve the linear equations and get the coefficients of the polynomial
    coefficients = list( np.linalg.solve(A,B) )

    # Results
    p = Polynomial(coefficients=coefficients)
    p.show(low=a,high=b,toShow=False)
    xPoints = list(np.linspace(a,b,100))
    yPoints = list(map(f,xPoints))
    plt.plot(xPoints,yPoints,'r:',linewidth='2.2',label='sin(x) + cos(x)')
    plt.title("best fit polynomial")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.legend()
    plt.show()


if __name__=='__main__':

    givenFunction = lambda x : math.sin(x) + math.cos(x)
    bestFitFunction( f = givenFunction, n = 5 )