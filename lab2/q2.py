from q1 import UndirectedGraph
from random import random


class ERRandomGraph(UndirectedGraph):

    def __init__(self, numVertices=None) -> None:
        super().__init__(numVertices)

    def sample(self, probability):

        for u in range(1, self.numVertex+1):
            for v in range(u+1, self.numVertex+1):
                randNum = random()
                if (randNum < probability):
                    self.addEdge(u, v)


if __name__ == '__main__':
    g = ERRandomGraph(100)
    g.sample(0.7)
    g.plotDegDist()
