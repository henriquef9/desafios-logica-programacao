import heapq

def carPooling(trips, capacity):

    heap = []

    for i in range(len(trips)):
        heap.append((trips[i][1], trips[i][0]))
        heap.append((trips[i][2], -trips[i][0])) 

    heapq.heapify(heap)

    current_capacity = capacity

    for _ in range(len(heap)):
        current_trip = heapq.heappop(heap)
        
        current_capacity -= current_trip[1]

        if current_capacity < 0:
            return False
    

    return True






print(carPooling([[2,1,5],[3,5,7]], 3))