class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        ans = -float('inf')
        for point in points:
            x = point[0]
            y = point[1]
            while len(heap) and abs(heap[0][1]-x) > k:
                heapq.heappop(heap)
            if len(heap):
                ans = max(ans,x+y+(-heap[0][0]))
            heapq.heappush(heap,(-(y-x),x))
        return ans
        