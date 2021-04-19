import statistics
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        myHeap = []
        medium =  arr[( len(arr)-1 )//2]
        
        for val in arr:
            heapq.heappush(myHeap,(abs(val-medium),val))
            if len(myHeap) > k:
                heapq.heappop(myHeap)
        return [val[1] for val in myHeap]