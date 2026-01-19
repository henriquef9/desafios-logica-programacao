import heapq
from collections import deque

# union find

class DisjointSets:

    def __init__(self, size):

        self.ds = [i for i in range(size)]

    def set(self, elem):

        if self.ds[elem]!=elem:

            self.ds[elem] = self.set(self.ds[elem])

        return self.ds[elem]



    def union(self, elem1, elem2):

        self.ds[ self.set(elem1) ] = self.set(elem2)




class Graph:

    def __init__(self, V):

        self.V = V

        self.E = 0

        self.adj = [[] for _ in range(V)]



    def add_edge(self, u, v, w):

        self.adj[u].append((v, w))


    def Kruskal(self):

        edges = []

        for u in range(self.V):

            for v, weight in self.adj[u]:

                edges.append( (weight, u, v) )

        edges.sort()

        
        colors = DisjointSets(self.V)

        mst_sum = 0

        for weight, u, v in edges:

            if colors.set(u)!=colors.set(v):

                mst_sum += weight

                colors.union(u,v)

        return mst_sum


def minCostConnectPoints(points):

    G = Graph(len(points))

    for i in range(len(points)):
        for j in range(i+1,len(points)):
            distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            G.add_edge(i, j, distance)
            G.add_edge(j, i, distance)
    
    return G.Kruskal()


print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))