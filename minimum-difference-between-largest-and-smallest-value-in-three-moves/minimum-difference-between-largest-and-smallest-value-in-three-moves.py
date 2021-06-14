class Solution:
    def minDifference(self, nums: List[int]) -> int:
        dp = {}
        nums.sort()
        def helper(L,R,k):
            if L == R:
                return 0
            if k == 0:
                return abs(nums[L]-nums[R])
            return min(helper(L+1,R,k-1),helper(L,R-1,k-1))
        return helper(0,len(nums)-1,3)