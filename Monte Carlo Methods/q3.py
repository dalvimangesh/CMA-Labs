import matplotlib.pyplot as plt
from random import uniform as random
import math


def estimatePi(numberOfExpts):
    '''
    This function estimates the value of pi using the Monte Carlo method.
    The method involves generating random points within a square of side length 2,
    with the circle of radius 1 and origin at (0,0) inscribed in the square.
    The ratio of points inside the circle to the total number of points generated
    is used to estimate pi.
    '''

    estimate = []

    totalPoints = 0
    pointsInsideCircle = 0

    for _ in range(numberOfExpts):

        x = random(-1.0, 1.0)
        y = random(-1.0, 1.0)


        # circle equation with centre at origin (0,0) => r*2 = x * x + y * y
        res = x * x + y * y

        # checking if points lies inside circle or not
        if ( res * res) <= 1.0:
            pointsInsideCircle += 1

        totalPoints += 1

        estimate.append(4 * (pointsInsideCircle / totalPoints))

    # Plotting the estimated values of pi against the true value of pi from the math library
    plt.plot(estimate,color='tab:blue',label='Monte Carlo method')
    plt.plot([math.pi]*len(estimate),color='tab:red' ,label='Value of math.pi',lw='2')
    plt.ylim(3.10, 3.20)
    plt.xlabel('No. of points generated')
    plt.ylabel('4 x fraction of points within the circle')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == '__main__':
    noOfExpt = 2000000
    estimatePi(noOfExpt)
