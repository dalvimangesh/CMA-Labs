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

    # Assuming in free graph there can be max inf vertex
    @Check
    def __init__(self, numVertices=None) -> None:

        self.maxNumVertex = inf if numVertices is None else numVertices
        self.isFree = False # to store graph is free not
        self.adjList = dict() # adjacency list
        self.numVertex = numVertices # number of vertex present
        self.numEdges = 0 # number of edges present
        if self.maxNumVertex < 0:
            raise Exception('Node index cannot exceed number of nodes\n')

        if numVertices is None:
            self.isFree = True
            self.numVertex = 0

        if not self.isFree: # creating adjList for each node if graph is not free
            for i in range(1, self.maxNumVertex+1):
                self.adjList[i] = set()

    # to function the whole graph in given format
    def __str__(self) -> str:

        info = f"Graph with {self.numVertex} nodes and {self.numEdges} edges. Neighbours of the nodes are belows:\n"

        for node, neighbours in self.adjList.items():
            if len(neighbours):
                info += f"Node {node}: { str(neighbours) }\n"
            else:
                info += f"Node {node}: {{}}\n"

        return info

    '''
    overloaing '+' operator
    >>> g = g + 10
    >>> g = g + (12, 15)
    '''
    def __add__(self, val=None) -> None:

        if type(val) is int:
            self.addNode(val)

        elif type(val) is tuple and len(val) == 2:
            self.addEdge(val[0], val[1])

        else:
            raise Exception('addition possible only with integer or tuple of length 2')

        return self

#Private Methods

    # function to check if node is valid is or not
    def __checkNode(self, node) -> bool:
        if node is None or node > self.maxNumVertex or node <= 0:
            return False
        return True

    # Function returns degreeDistribution for each degree and avgerage degreeDistribution
    def __findFractionDegree(self):

        degreeDistribution = dict()
        avg = 0

        # Max degree can be numVertex-1, initializing all possible degree to zero
        for degree in range(self.numVertex):
            degreeDistribution[degree] = 0

        # Finding degree distribution

        for _, value in self.adjList.items():
            degreeDistribution[len(value)] += 1
            avg += len(value)

        for i in degreeDistribution:
            degreeDistribution[i] = degreeDistribution[i]/self.numVertex

        avg = avg / self.numVertex

        return degreeDistribution, avg

    def __BFS(self, start, visited):

        '''
        Function to do bfs from start vertex and using current visited set
        return number of vertex visited and which are visited
        '''

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

#Public Methods

    # function to add node in current graph if it is valid
    @Check
    def addNode(self, node=None) -> None:

        if not self.__checkNode(node):
            raise Exception('Node index cannot exceed number of nodes')

        if node not in self.adjList:
            self.adjList[node] = set()
            self.numVertex += 1

    # function to add edge in current graph if it is valid
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

        # plotting the degree distribution 1 of a graph

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

    # function returns true if graph is connected ( checks using BFS )
    def isConnected(self) -> bool:

        if self.numVertex == 0:
            return True

        startNode = None

        for node in self.adjList:
            startNode = node
            break

        visited = set()

        self.__BFS(start=startNode, visited=visited) # doing BFS

        # if all vertex get visited means it is connected
        if len(visited) == self.numVertex:
            return True

        return False

    # Function to return size of largest and second largest component in graph
    def oneTwoComponentSizes(self):

        visited = set()
        sizes = [0, 0]

        for vertex in self.adjList:

            if vertex not in visited:
                count, visited = self.__BFS(start=vertex, visited=visited)
                sizes.append(count)

        sizes.sort()

        return [sizes[-1], sizes[-2]]

# derived class from UndirectedGraph Class to create a Erdos-Renyi random graph
class ERRandomGraph(UndirectedGraph):

    def __init__(self, numVertices=None) -> None:
        super().__init__(numVertices)

    # Generates a random graph with given probability p
    def sample(self, probability):

        for u in range(1, self.numVertex+1):
            for v in range(u+1, self.numVertex+1):
                randNum = random()
                # adding edge with given probability
                if (randNum < probability):
                    self.addEdge(u, v)


def VerifyErdosRenyl():

    '''
    to verify : If p < 0.001, the Erdős-Rényi random graph G(1000, p) will almost surely have only
    small connected components. On the other hand, if p > 0.001, almost surely, there will be
    a single giant component containing a positive fraction of the vertices
    '''

    runs = 50 # Number of runs for each probability
    p = 0.0  # to iterate over all probability
    epsilon = 0.0002 # small value
    limit = 0.01 + epsilon

    # The theoretical threshold for largest connected component which is 1 / n
    largestCCThreshold = 1 / 1000

    # The theoretical Connectedness threshold which is log(n) / n
    connectedThreshold = (1 - epsilon) * (math.log(1000,math.e)) / 1000

    xPoints = []
    y1Points = []
    y2Points = []

    # Running loop until p reaches limit , increating value in p by epsilon in each interation
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
        
        # fraction for Largest connected component
        y1Points.append(countLargest/runs)
        # fraction for 2nd largest connected component
        y2Points.append(countSecondLargest/runs)
        xPoints.append(p)

        p += epsilon

    plt.plot(xPoints,y1Points,color='green',label='Largest connected component')
    plt.plot(xPoints,y2Points,color='blue',label='2nd largest connected component')
    plt.axvline(x=largestCCThreshold,color='red',label='Largest CC size threshold')
    plt.axvline(x=connectedThreshold,color='tab:orange',label='Connectedness threshold')
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
