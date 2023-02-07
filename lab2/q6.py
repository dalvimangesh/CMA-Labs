from q5 import Lattice
import matplotlib.pyplot as plt

def VarifyBondPercolation():

    '''
    to verify : A path exists (almost surely) from the top-most layer to the bottom-most 
    layer of a 100*100 grid graph only if the bond percolation probability exceeds 0.5
    '''

    p = 0.0 # to iterate over all probability
    epsilon = 0.02 # small value
    runs = 50 # Number of runs for each probability
    limit = 1

    xPoints = []
    yPoints = []

    # Running loop until p reaches limit , increating value in p by epsilon in each interation
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

    plt.plot(xPoints,yPoints,"b")
    plt.title('Critical cut-off in 2-D bond percolation')
    plt.xlabel('p')
    plt.ylabel('Fraction of runs end-to-end percolation occurred')
    plt.grid()
    plt.show()

if __name__=='__main__':

    VarifyBondPercolation()
