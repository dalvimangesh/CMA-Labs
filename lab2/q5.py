import networkx as nx
import matplotlib.pyplot as plt
from random import random
import sys

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

class Lattice:

    @Check
    def __init__(self, n=None) -> None:

        if n is None:
            raise Exception('n is mandatory argument\n')

        if n < 0:
            raise Exception('n should be non negative\n')

        self.n = n # number of rows and columns
        self.graph = nx.grid_2d_graph(n, n) # creating 2d grid of n*n
        self.__removeAllEdges() # Creating empty lattice

# Private

    def __removeAllEdges(self):
        nodes = self.graph.edges()
        for u, v in nodes: self.graph.remove_edge(u, v)
        self.pos = dict(((x, y), (y, -x)) for x, y in self.graph.nodes())

    def __BFS(self, start) -> None:

        bfs_tree = nx.bfs_tree(self.graph, start) # doing bfs on graph using inbuilt function

        source = None # to store longest path vertex
        deep = -1 # to store longest distance

        # getting the deepest vertex by comparing coordinate with from start node
        for node in bfs_tree.nodes():
            if node[0] > deep:
                deep = node[0]
                source = node
        
        # edges in the shortest path of longest distance vertex
        edges = nx.shortest_path(bfs_tree, start, source)
        
        edgeList = []

        for i in range(len(edges)-1):
            edgeList.append((edges[i], edges[i+1]))

        nx.draw_networkx_edges(self.graph, pos=self.pos, edgelist=edgeList, edge_color='green')

# Public

    # function to plot current graph
    def show(self, plot=True):
        nx.draw(self.graph, self.pos, with_labels=False, node_color='blue', node_size=0.30, edge_color='red')
        if plot:
            plt.show()

    # to create random graph
    def percolate(self, p) -> None:

        self.__removeAllEdges()

        # to avoid double counting , adding to bottom and left
        dx, dy = [1, 0], [0, -1] 

        def isValidPoint(i, j) -> bool:
            if i < 0 or j < 0 or i >= self.n or j >= self.n:
                return False
            return True

        for u, v in self.graph.nodes():
            for i in range(2):
                # co-ordinate of neighbours
                newx, newy = dx[i] + u, dy[i] + v
                randNum = random()
                if isValidPoint(newx, newy):
                    if randNum < p:
                        self.graph.add_edge((u, v), (newx, newy))
        
        self.pos = dict(((x, y), (y, -x)) for x, y in self.graph.nodes())

    # function  returns true if there a path from first row to last rowf
    def existsTopDownPath(self):

        for i in range(self.n):
            for j in range(self.n):
                if nx.has_path(self.graph,(0,i),(self.n-1,j)):
                    return True

        return False

    '''
    function to do bfs from each vertex of first row
    and ploting the shortest distance to the longest path vertex
    '''
    def showPaths(self):

        self.show(False)
        u = 0
        for v in range(self.n):
            
            self.__BFS((u, v))
        plt.show()


if __name__ == '__main__':

    l = Lattice(100)
    l.percolate(0.7)
    l.showPaths()
