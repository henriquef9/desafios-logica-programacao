

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


def findRedundantConnection(edges):

    dsu = DisjointSets(len(edges))

    redundant_edge = None

    for u,v in edges:

        if dsu.set(u-1) != dsu.set(v-1):
            dsu.union(u-1,v-1)
        else:
            redundant_edge = [u,v]
    
    return redundant_edge