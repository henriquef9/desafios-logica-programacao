import heapq

class Graph:

    def __init__(self, V):

        self.V = V

        self.E = 0

        self.adj = [[] for _ in range(V)]



    def add_edge(self, u, v, w):

        self.adj[u].append((v, w))


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





def networkDelayTime(times, n, k):


    G = Graph(n)

    for u,v,w in times:
        G.add_edge(u-1,v-1,w)


    distance_min = G.Dijkstra(k-1)

    max_distance = max(distance_min)

    if max_distance == float("inf"):
        return -1
    else:
        return max_distance



print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
   