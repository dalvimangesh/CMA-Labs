import matplotlib.pyplot as plt
from random import uniform as random
import math

def estimatePi(numberOfExpts):

    '''
        consider the circle of radius 1 and origin at (0,0)
    '''

    estimate = []

    totalPoints = 0
    pointsInsideCircle = 0

    for _ in range(numberOfExpts):

        x = random(-1.0,1.0)
        y = random(-1.0,1.0)

        res = x * x + y * y

        if res <= 1.0:
            pointsInsideCircle += 1

        totalPoints+=1

        estimate.append( 4 * ( pointsInsideCircle / totalPoints ) )

    plt.plot(estimate,'b')
    plt.plot([math.pi]*len(estimate),'r')
    plt.ylim(3.10, 3.20)
    plt.show()

estimatePi(2000000)
