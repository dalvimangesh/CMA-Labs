from q5 import Lattice
import matplotlib.pyplot as plt

def VarifyBondPercolation():

    p = 0.0
    epsilon = 0.05 # small value
    runs = 50
    limit = 1

    xPoints = []
    yPoints = []

    while p <= limit:

        print('P = ',p)

        count = 0

        for _ in range(runs):

            l = Lattice(100) # empty 100*100 graph
            l.percolate(p) # adding edges with probability p
            if l.existsTopDownPath():
                count += 1

        xPoints.append(p) # current probability
        yPoints.append(count/runs) # storing the average

        p += epsilon # increating p by small value

    plt.plot(xPoints,yPoints)
    plt.title('Critical cut-off in 2-D bond percolation')
    plt.xlabel('p')
    plt.ylabel('Fraction of runs end-to-end percolation occurred')
    plt.grid()
    plt.show()

if __name__=='__main__':

    VarifyBondPercolation()