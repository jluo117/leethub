class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        myHeap = []
        maxRooms = 0
        for interval in intervals:
            if len(myHeap) == 0 or myHeap[0] > interval[0]:
                heapq.heappush(myHeap,interval[1])
            else:
                heapq.heappop(myHeap)
                heapq.heappush(myHeap,interval[1])
            maxRooms = max(len(myHeap),maxRooms)
        return maxRooms
            
        