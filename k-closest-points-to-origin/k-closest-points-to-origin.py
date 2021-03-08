class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myHeap = []
        for point in points:
            dis = (point[0] * point[0]) + (point[1]*point[1])
            heapq.heappush(myHeap,(-dis,point))
            if len(myHeap) > k:
                heapq.heappop(myHeap)
        return [i[1] for i in myHeap]
        