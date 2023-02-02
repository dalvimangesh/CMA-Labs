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

    def __BFS(self,start,visited):
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
            
        return count,visited

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

        self.__BFS(start = startNode,visited=visited)

        if len(visited) == self.numVertex:
            return True

        return False


class ERRandomGraph(UndirectedGraph):

    def __init__(self, numVertices=None) -> None:
        super().__init__(numVertices)

    def sample(self, probability):

        for u in range(1, self.numVertex+1):
            for v in range(u+1, self.numVertex+1):
                randNum = random()
                if (randNum < probability):
                    self.addEdge(u, v)


def VerifyErdosRenyi():

    runs = 1000

    epsilon = 0.002
    p = 0.0
    constant = math.log(100,math.e) / 100
    limit = 0.1 + epsilon

    xPoints = []
    yPoints = []

    while p <= limit:

        print(p)

        count = 0

        for _ in range(runs):
            g = ERRandomGraph(100)
            g.sample(p)
            if g.isConnected():
                count += 1

        xPoints.append(p)
        yPoints.append(count/1000)

        p += epsilon


    plt.plot(xPoints,yPoints,color="blue")
    plt.axvline(x=constant,color="red",label='Theoretical threshold')
    plt.title('Connectedness of a G(100, p) as function of p')
    plt.xlabel('p')
    plt.ylabel('fraction of runs G(100, p) is connected')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':

    g = UndirectedGraph(5)
    g = g + (1, 2)
    g = g + (2, 3)
    g = g + (3, 4)
    g = g + (3, 5)
    print(g.isConnected())

    g = UndirectedGraph(5)
    g = g + (1, 2)
    g = g + (2, 3)
    g = g + (3, 5)
    print(g.isConnected())
    print(g)

    VerifyErdosRenyi()
