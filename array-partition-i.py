class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        maxHeap = []
        minHeap = []
        for num in nums:
            heapq.heappush(maxHeap,-num)
            
        rem = len(nums)/2
        runningSum = 0
        while rem > 0:
            front = -heapq.heappop(maxHeap)
            back = -heapq.heappop(maxHeap)
            runningSum += min(front,back)
            rem -= 1
        return runningSum
