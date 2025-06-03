import heapq

def deleteGreatestValue(grid):
        list_heaps = []

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            list_heaps.append([ (-grid[i][j], j) for j in range(n) ])
            heapq.heapify(list_heaps[i])

        soma = 0
        for i in range(n):
            max_value = - 1
            for j in range(m):
                heap = list_heaps[j]
                max_extract = heapq.heappop(heap)
                if -max_extract[0] > max_value:
                    max_value = -max_extract[0]
            soma += max_value
        
        return soma







print(deleteGreatestValue([[10]]))