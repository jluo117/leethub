class SparseVector:
    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.index_map = {}
        for index in range(len(nums)):
            if nums[index] != 0:
                self.index_map[index] = nums[index]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for index in self.index_map:
            if index in vec.index_map:
                res += self.index_map[index] * vec.index_map[index]
        return res
            
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)