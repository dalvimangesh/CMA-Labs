import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import romberg
from q1 import Polynomial

def bestFitFunction(f,n,a,b) -> None:

    A = []
    B = []

    for j in range(0,n+1):
        curRow = []
        for k in range(0,n+1):
            curFun = lambda x : x**(j+k)
            curRow.append(romberg(function=curFun,a=a,b=b))
        A.append(curRow)

    for j in range(0,n+1):
        curFun = lambda x : (x**j) * f(x)
        B.append(romberg(function=curFun,a=a,b=b))

    coefficients = list( np.linalg.solve(A,B))

    p = Polynomial(coefficients=coefficients)
    p.show(low=a,high=b,toShow=False)

    xPoints = list(np.linspace(a,b,100))
    yPoints = list(map(f,xPoints))
    
    plt.plot(xPoints,yPoints,'r:',linewidth='2.2')

    plt.show()


if __name__=='__main__':

    givenFunction = lambda x : math.sin(x) + math.cos(x)
    bestFitFunction( f = givenFunction, n = 5, a = 0, b = math.pi )
