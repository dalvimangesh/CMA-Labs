import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from q1 import Polynomial

def forwardEulerMethod(ode,originalSol,hlist,x0,a,b):


    for h in hlist:

        xPoints = [x0]
        points = [(0,x0)]
        tPoints = list( np.arange( a,b,h ) )

        for i in range( 1 , len(tPoints) ):

            xPoints.append(  ode( tPoints[i-1], xPoints[i-1], h)  )

            points.append( ( tPoints[i], xPoints[i] ) )

        p = Polynomial([0])
        p.fitViaMatrixMethod(points=points)


    xPoints = list(np.linspace(a,b,100))
    yPoints = list( map( originalSol, xPoints ) )
    print(yPoints)
    plt.plot(xPoints,yPoints,color='red')

    plt.ylim(-6,6)
    plt.show()

if __name__=='__main__':

    def givenODE(t,x,h) : return (x / ( 1 + 2*h ) )

    def originalSol (x) : return math.exp(-2*x) * 5

    hlist = [0.1, 0.5, 1, 2, 3]

    x0 = 5

    forwardEulerMethod( ode=givenODE, originalSol=originalSol, hlist=hlist, x0=x0, a=0, b=10)
