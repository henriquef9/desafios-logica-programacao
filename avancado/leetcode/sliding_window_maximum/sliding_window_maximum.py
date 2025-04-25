import heapq

def maxSlidingWindow(nums, k):
    
    maxHeap = [(-nums[i], i) for i in range(k)]

    heapq.heapify(maxHeap)
    output = []
    startWindow = 0
    endWindow = k - 1

    while endWindow < len(nums):
        while True:
            maxVal, index = maxHeap[0]
            if index <= startWindow:
                break
            heapq.heappop(maxHeap)
        output.append(-maxVal)
        startWindow += 1
        endWindow += 1
        if endWindow < len(nums):
            heapq.heappush(maxHeap, (- nums[endWindow], endWindow))
    return output



nums = [1,3,-1,-3,5,3,6,7]
k = 4
print(maxSlidingWindow(nums, k))