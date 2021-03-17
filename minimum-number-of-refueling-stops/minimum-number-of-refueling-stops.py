class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        curLoc = 0
        curFuel = startFuel
        moves = 0
        stations.append((target,float('inf')))
        stationHeap = []
        for station in stations:
            curFuel -= station[0] - curLoc
            while len(stationHeap) > 0 and curFuel < 0:
                curFuel += -heapq.heappop(stationHeap)
                moves += 1
            if curFuel < 0:
                return -1
            heapq.heappush(stationHeap,-station[1])
            curLoc = station[0]
        return moves
        
        