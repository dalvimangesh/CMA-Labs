from q1 import UndirectedGraph
from random import random
import sys

# derived class from UndirectedGraph Class to create a Erdos-Renyi random graph
class ERRandomGraph(UndirectedGraph):

    def __init__(self, numVertices=None) -> None:
        super().__init__(numVertices)

    # Generates a random graph with given probability p
    def sample(self, probability):

        try:
            if probability < 0 or probability > 1:
                raise Exception('Probability should be non negative and less than equal to 1')
        except Exception as e:
            print(type(e))
            print(e)
            sys.exit(-1)

        for u in range(1, self.numVertex+1):
            for v in range(u+1, self.numVertex+1):
                randNum = random()
                # adding edge with given probability
                if (randNum < probability):
                    self.addEdge(u, v)


if __name__ == '__main__':
    g = ERRandomGraph(100)
    g.sample(0.7)
    g.plotDegDist()