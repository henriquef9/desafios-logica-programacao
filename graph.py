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


    def BFS(self, source):

        visited = [False] * self.V

        queue = deque([source])

        visited[source] = True
        

        while queue:
            node = queue.popleft()

            for neigh, _ in self.adj[node]:

                if not visited[neigh]:

                    visited[neigh] = True

                    queue.append(neigh)
                    

    def DFS(self, source):

        visited = [False] * self.V

        stack = [source]

        while stack:

            node = stack.pop()

            if not visited[node]:

                visited[node] = True

                for neigh, _ in self.adj[node]:

                    if not visited[neigh]:

                        stack.append(neigh)


    def Dijkstra(self, source):

        d = [float("inf")] * self.V # O(V)

        d[source] = 0

        min_heap = [(0, source)]



        while min_heap: #O(V)

            cost, working_node = heapq.heappop(min_heap) # O(VlogV)

            if cost>d[working_node]: continue


            for neigh, weight in self.adj[working_node]: #O(E)

                if d[working_node] + weight < d[neigh]:

                    d[neigh] = d[working_node] + weight

                    heapq.heappush(min_heap, (d[neigh], neigh))

        return d


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
    
    def Prim(self):
        visited = [False]*self.V
        dist = [float("inf") for _ in range(self.V)]
        dist[0] = 0 #0 vai ser o inicial
        min_heap = [(0,0)] #cost/node

        sum_dist = 0

        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if visited[node]: continue
            visited[node] = True

            for neigh, weigth in self.adj[node]:
                if weigth < dist[neigh]:
                    dist[neigh] = weigth
                    sum_dist += weigth
                    heapq.heappush(min_heap, (weigth, neigh))
        return sum_dist