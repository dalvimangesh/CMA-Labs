import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad


def fourierApproximation(n=10):

    '''
    function to compute coefficients of the best-fit Fourier approximation Sn(x) of function
    e^x in the interval [−π, π].
    '''

    try:
        if n < 0: raise Exception('n should be non negative')
    except Exception as e:
        print(type(e))
        print(e)
        exit(-1)

    a = -math.pi
    b = math.pi
    A,B = [],[]

    f = lambda x : math.exp(x)

    # Compute the Fourier coefficients
    for k in range(0,n+1):

        # for cos term
        curFun = lambda x : f(x) * math.cos(k*x) 
        A.append((1/math.pi)*quad(func=curFun,a=a,b=b)[0])

        # for sin term
        curFun = lambda x : f(x)*math.sin(k*x)
        B.append((1/math.pi)*quad(func=curFun,a=a,b=b)[0])

    # evaluate the original function and its Fourier series over 100 points
    xPoints = list(np.linspace(a,b,100))
    y1Points = list(map(f,xPoints))
    y2Points = []

    # Compute the Fourier series at each x value
    for x in xPoints:
        sum1, sum2 = 0,0

        for k in range(1,n+1):
            sum1 += A[k] * math.cos(k*x)
            sum2 += B[k] * math.sin(k*x)
        
        S = (A[0]/2) + sum1 + sum2
        y2Points.append(S)

    # Result
    plt.plot(xPoints,y1Points,label='eˣ')
    plt.plot(xPoints,y2Points,label='Fourier approx')
    plt.title("best fit polynomial")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':

    print(fourierApproximation())
