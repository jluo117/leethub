class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = []
        for p,s in zip(position,speed):
            fleets.append((p,s))
        fleets.sort()
        resHeap = []
        for fleet in fleets:
            gap = target - fleet[0]
            
            time = (gap/fleet[1])
            
            while resHeap and resHeap[0] <= time:
                heapq.heappop(resHeap)
            heapq.heappush(resHeap,time)
        return len(resHeap)