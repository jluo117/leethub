'''
3,4,5,5
​
'''
class KthLargest:
​
    def __init__(self, k: int, nums: List[int]):
        self.myHeap = []
        for num in nums:
            self.myHeap.append(num)
        self.k = k
        heapify(self.myHeap)
        while len(self.myHeap) > self.k:
            heappop(self.myHeap)
        
​
    def add(self, val: int) -> int:
        heappush(self.myHeap,val)
        while len(self.myHeap) > self.k:
            heappop(self.myHeap)
        return self.myHeap[0]
​
​
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
