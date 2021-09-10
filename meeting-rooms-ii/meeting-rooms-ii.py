class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cur_heap = []
        max_size = 0
        for interval in intervals:
            while len(cur_heap) and cur_heap[0] <= interval[0]:
                heapq.heappop(cur_heap)
            heapq.heappush(cur_heap,interval[1])
            max_size = max(len(cur_heap),max_size)
        return max_size