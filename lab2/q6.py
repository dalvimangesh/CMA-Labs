from q5 import Lattice
import matplotlib.pyplot as plt

def Varify():

    p = 0.0
    epsilon = 0.03
    runs = 5

    limit = 1
    xPoints = []
    yPoints = []

    while p <= limit:
        print(p)

        count = 0

        for _ in range(runs):

            l = Lattice(100)
            l.percolate(p)
            if l.existsTopDownPath():
                count += 1

        print(count)

        xPoints.append(p)
        yPoints.append(count/runs)

        p += epsilon

    plt.plot(xPoints,yPoints)
    plt.show()


Varify()