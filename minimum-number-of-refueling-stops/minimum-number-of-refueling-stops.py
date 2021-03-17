class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        myHeap = []
        curLoc = 0
        curFuel = startFuel
        stops = 0
        stations.append((target,float('inf')))
        for station in stations:
            curFuel -= station[0] - curLoc
            while len(myHeap) and curFuel < 0:
                curFuel += -heapq.heappop(myHeap)
                stops += 1
            if curFuel < 0:
                return -1
            
            heapq.heappush(myHeap,-station[1])
            curLoc = station[0]
        return stops
            
                
                
        