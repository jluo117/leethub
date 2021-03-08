class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        myHeap = []
        for val in freq:
            heapq.heappush(myHeap,(freq[val],val))
            if len(myHeap) > k:
                heapq.heappop(myHeap)
        return [i[1] for i in myHeap]
        