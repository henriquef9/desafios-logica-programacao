import heapq

def nthUglyNumber(n):

    heap = [1]

    seen = {1}

    for _ in range(n):

        min_ugly = heapq.heappop(heap)

        for limited in [2,3,5]:
            new = limited * min_ugly

            if new not in seen:
                seen.add(new)
                heapq.heappush(heap, new)
    
    return min_ugly


print(nthUglyNumber(10))