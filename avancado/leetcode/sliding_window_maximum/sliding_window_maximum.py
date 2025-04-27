import heapq
from collections import deque

# def maxSlidingWindow(nums, k):
    
#     maxHeap = [(-nums[i], i) for i in range(k)]

#     heapq.heapify(maxHeap)
    
#     output = []
#     startWindow = 0
#     endWindow = k - 1

#     while endWindow < len(nums):
#         while True:
#             maxVal, index = maxHeap[0]
#             if index >= startWindow:
#                 break
#             heapq.heappop(maxHeap)
        
#         output.append(-maxVal)
#         startWindow += 1
#         endWindow += 1
#         if endWindow < len(nums):
#             heapq.heappush(maxHeap, (- nums[endWindow], endWindow))

#     return output
        
    
def maxSlidingWindow(nums, k):

    fila = deque()

    output = []
    startWindow = 0
    endWindow = k - 1


    for i in range(0, k):

        while fila and fila[-1][0] < nums[i]:
            fila.pop()

        fila.append((nums[i], i))
    
    output.append(fila[0][0])

    if fila[0][1] == startWindow:
        fila.popleft()

    startWindow+=1
    endWindow+=1
        
    while endWindow < len(nums):

        while fila and fila[-1][0] < nums[endWindow]:
            fila.pop()

        fila.append((nums[endWindow], endWindow))

        output.append(fila[0][0])

        if fila[0][1] == startWindow:
            fila.popleft()

        startWindow+=1
        endWindow+=1

    return output






nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums, k))