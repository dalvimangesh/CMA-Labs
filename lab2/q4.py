import matplotlib.pyplot as plt
from random import random
from queue import Queue
import math

import sys
global inf
inf = 1000

# Function to check for any exception in inputFunction
def Check(inputFunction):

    # Function to handle the exception
    def newFunction(ref, *arg, **kwargs):
        try:
            inputFunction(ref, *arg, **kwargs)
        except Exception as e:
            print(type(e))
            print(e)
            sys.exit(-1)

    return newFunction


class UndirectedGraph:

    def __init__(self, numVertices=None) -> None:

        self.maxNumVertex = inf if numVertices is None else numVertices
        self.isFree = False
        self.adjList = dict()
        self.numVertex = numVertices
        self.numEdges = 0
        if self.maxNumVertex < 0:
            raise Exception('Node index cannot exceed number of nodes\n')

        if numVertices is None:
            self.isFree = True
            self.numVertex = 0

        if not self.isFree:
            for i in range(1, self.maxNumVertex+1):
                self.adjList[i] = set()

    def __str__(self) -> str:

        info = f"Graph with {self.numVertex} nodes and {self.numEdges} edges. Neighbours of the nodes are belows:\n"

        for node, neighbours in self.adjList.items():
            if len(neighbours):
                info += f"Node {node}: { str(neighbours) }\n"
            else:
                info += f"Node {node}: {{}}\n"

        return info

    def __add__(self, val=None) -> None:

        if type(val) is int:
            self.addNode(val)

        elif type(val) is tuple and len(val) == 2:
            self.addEdge(val[0], val[1])

        else:
            raise Exception(
                'addition possible only with integer or tuple of length 2')

        return self

    def __checkNode(self, node) -> bool:
        if node is None or node > self.maxNumVertex or node <= 0:
            return False
        return True

    def __findFractionDegree(self):

        degreeDistribution = dict()
        avg = 0

        for degree in range(self.numVertex):
            degreeDistribution[degree] = 0

        for _, value in self.adjList.items():
            degreeDistribution[len(value)] += 1
            avg += len(value)

        for i in degreeDistribution:
            degreeDistribution[i] = degreeDistribution[i]/self.numVertex

        avg = avg / self.numVertex

        return degreeDistribution, avg

    def __BFS(self, start, visited):
        count = 0
        q = Queue()
        q.put(start)
        visited.add(start)
        while q.qsize():
            ele = q.get()
            count += 1
            for neighbour in self.adjList[ele]:
                if neighbour not in visited:
                    q.put(neighbour)
                    visited.add(neighbour)

        return count, visited

    @Check
    def addNode(self, node=None) -> None:

        if not self.__checkNode(node):
            raise Exception('Node index cannot exceed number of nodes')

        if node not in self.adjList:
            self.adjList[node] = set()
            self.numVertex += 1

    @Check
    def addEdge(self, u=None, v=None):

        self.addNode(u)
        self.addNode(v)

        self.adjList[u].add(v)
        self.adjList[v].add(u)

        self.numEdges += 1

        return

    @Check
    def plotDegDist(self):

        degreeDistribution, avg = self.__findFractionDegree()

        xPoints = []
        yPoints = []

        for key, value in degreeDistribution.items():
            xPoints.append(key)
            yPoints.append(value)

        plt.axvline(x=avg, color='red', label='Avg. node degree')
        plt.plot(xPoints, yPoints, "o", color="tab:blue",
                 label='Actual degree distribution')
        plt.grid()
        plt.xlabel('Node degree')
        plt.ylabel('Fraction of Nodes')
        plt.title('Node Degree Distribution')
        plt.legend()
        plt.show()

    def isConnected(self) -> bool:

        if self.numVertex == 0:
            return True

        startNode = None

        for node in self.adjList:
            startNode = node
            break

        visited = set()

        self.__BFS(start=startNode, visited=visited)

        if len(visited) == self.numVertex:
            return True

        return False

    def oneTwoComponentSizes(self):

        visited = set()
        sizes = [0, 0]

        for vertex in self.adjList:

            if vertex not in visited:
                count, visited = self.__BFS(start=vertex, visited=visited)
                sizes.append(count)

        sizes.sort()

        return [sizes[-1], sizes[-2]]


class ERRandomGraph(UndirectedGraph):

    def __init__(self, numVertices=None) -> None:
        super().__init__(numVertices)

    def sample(self, probability):

        for u in range(1, self.numVertex+1):
            for v in range(u+1, self.numVertex+1):
                randNum = random()
                if (randNum < probability):
                    self.addEdge(u, v)


'''
If p < 0.001, the Erdős-Rényi random graph G(1000, p) will almost surely have only
small connected components. On the other hand, if p > 0.001, almost surely, there will be
a single giant component containing a positive fraction of the vertices
'''


def VerifyErdosRenyl():

    runs = 50
    p = 0.0
    epsilon = 0.0002
    limit = 0.01 + epsilon
    LargestCCThreshold = 1 / 1000
    ConnectedThreshold = (1 - epsilon) * (math.log(1000)) / 1000

    xPoints = []
    y1Points = []
    y2Points = []

    while p <= limit:
        print(p)
        countLargest = 0
        countSecondLargest = 0

        for _ in range(runs):

            g = ERRandomGraph(1000)
            g.sample(p)
            sizes = g.oneTwoComponentSizes()

            countLargest += sizes[0]/1000
            countSecondLargest += sizes[1]/1000

        y1Points.append(countLargest/runs)
        y2Points.append(countSecondLargest/runs)
        xPoints.append(p)

        p += epsilon

    plt.plot(xPoints,y1Points,color='green',label='Largest connected component')
    plt.plot(xPoints,y2Points,color='blue',label='2nd largest connected component')
    plt.axvline(x=LargestCCThreshold,color='red',label='Largest CC size threshold')
    plt.axvline(x=ConnectedThreshold,color='tab:orange',label='Connectedness threshold')
    plt.grid()
    plt.show()


if __name__ == '__main__':

    # g = UndirectedGraph(6)
    # g = g + (1, 2)
    # g = g + (3, 4)
    # g = g + (6, 4)
    # print(g.oneTwoComponentSizes())

    # g = ERRandomGraph(100)
    # g.sample(0.01)
    # print(g.oneTwoComponentSizes())

    VerifyErdosRenyl()
