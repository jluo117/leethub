from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        table = Counter(arr)
        myHeap = []
        for val in table:
            heapq.heappush(myHeap,table[val])
        while k:
            if myHeap[0] > k:
                return len(myHeap)
            popVal = heapq.heappop(myHeap)
            k -= popVal
        return len(myHeap)