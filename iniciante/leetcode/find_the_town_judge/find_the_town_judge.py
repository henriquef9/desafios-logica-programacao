


class Graph:

    def __init__(self, V):

        self.V = V

        self.E = 0

        self.adj = [[] for _ in range(V)]



    def add_edge(self, u, v, w):

        self.adj[u].append((v, w))



def findJudge(n, trust):

    g = Graph(n)

    for u, v in trust:
        g.add_edge(u-1, v-1, 1)

    trusts_someone = [0]*n
    trusted_by = [0]*n

    for i in range(n):
        for j, _ in g.adj[i]:
            trusts_someone[i] += 1
            trusted_by[j] += 1

    for i in range(n):
        if trusts_someone[i] == 0 and trusted_by[i] == n-1:
            return i+1
    
    return -1



