import networkx as nx
import matplotlib.pyplot as plt
from random import random


class Lattice:

    def __init__(self, n=None) -> None:

        if n is None:
            raise Exception('n is mandantory argument\n')

        self.n = n
        self.graph = nx.grid_2d_graph(n, n)
        self.__removeAllEdges()

# Private

    def __removeAllEdges(self):
        nodes = self.graph.edges()
        for u, v in nodes:
            self.graph.remove_edge(u, v)

    def __BFS(self, start) -> bool:

        bfs_tree = nx.bfs_tree(self.graph, start)

        source = None

        length = 0
        for node in bfs_tree.nodes():
            curDis = nx.shortest_path_length(bfs_tree, start, node)
            if curDis > length:
                length = curDis
                source = node

        edges = nx.shortest_path(bfs_tree, start, source)
        flag = False
        edgeList = []

        for i in range(len(edges)-1):
            edgeList.append((edges[i], edges[i+1]))
            if edges[i][0] == self.n-1 or edges[i+1][0] == self.n-1:  # checking if path exists
                flag = True

        pos = dict(((x, y), (y, -x)) for x, y in self.graph.nodes())
        nx.draw_networkx_edges(self.graph, pos=pos, edgelist=edgeList, edge_color='green')
        return flag

# Public

    def show(self, plot=True):
        pos = dict(((x, y), (y, -x)) for x, y in self.graph.nodes())
        nx.draw(self.graph, pos, with_labels=False, node_color='blue', node_size=0.30, edge_color='red')
        if plot:
            plt.show()

    def percolate(self, p) -> None:

        self.__removeAllEdges()

        dx, dy = [1,0], [0,-1]

        def isValidPoint(i, j) -> bool:
            if i < 0 or j < 0 or i >= self.n or j >= self.n:
                return False
            return True

        for u, v in self.graph.nodes():
            for i in range(2):
                newx, newy = dx[i] + u, dy[i] + v
                randNum = random()
                if isValidPoint(newx, newy):
                    if randNum < p:
                        self.graph.add_edge((u, v), (newx, newy))

    def existsTopDownPath(self):

        u = 0
        for v in range(self.n):
            # print(v)
            if self.__BFS((u, v)):
                return True
        return False

    def showPaths(self):

        self.show(False)

        u = 0

        for v in range(self.n):
            print(v)
            self.__BFS((u, v))

        plt.show()


if __name__ == '__main__':

    l = Lattice(100)
    l.percolate(1)
    l.showPaths()
    # print(l.existsTopDownPath())