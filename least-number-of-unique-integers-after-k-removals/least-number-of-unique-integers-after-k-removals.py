class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrCounter = collections.Counter(arr)
        myHeap = []
        for val in arrCounter:
            heapq.heappush(myHeap,(arrCounter[val],val))
        while len(myHeap) and k >0:
            moveVal = min(myHeap[0][0],k)
            if myHeap[0][0] <= k:
                heapq.heappop(myHeap)
            k -= moveVal
        return len(myHeap)
            