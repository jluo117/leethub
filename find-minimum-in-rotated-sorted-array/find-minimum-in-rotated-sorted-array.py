class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) -1
        if nums[L] <= nums[R]:
                return nums[L]
        while L <= R:
            
            P = L + (R-L) // 2
            if nums[P+1] < nums[P]:
                return nums[P+1]
            if nums[P-1] > nums[P]:
                return nums[P]
            if nums[R] < nums[P]:
                L = P +1
            else:
                R = P
        
        