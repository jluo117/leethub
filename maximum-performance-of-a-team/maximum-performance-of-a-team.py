class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        sortVal = []
        for s,e in zip(speed,efficiency):
            sortVal.append((s,e))
        sortVal.sort(key = lambda x: x[1])
        
        myHeap = []
        cur = 0
        last = 0
        res = 0
        for vIndex in range(len(sortVal)-1,-1,-1):
            v = sortVal[vIndex]
            speed,eff = v
            if len(myHeap) >= k-1:
                if myHeap and last > myHeap[0]:
                    cur -= heappop(myHeap)
                    cur += last
                    heappush(myHeap,last)
            else:
                heapq.heappush(myHeap,last)
                cur += last
            last = speed
            res = max(res,(cur+speed)*eff)
                
            
        return res % (10 ** 9 + 7)
                
                
                
