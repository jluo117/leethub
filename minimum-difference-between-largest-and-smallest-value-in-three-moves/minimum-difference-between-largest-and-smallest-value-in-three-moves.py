class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        def helper(moves,L,R):
            if L == R:
                return 0
            if moves == 0:
                return abs(nums[L]-nums[R])
            return min(helper(moves-1,L+1,R),helper(moves-1,L,R-1))
        return helper(3,0,len(nums)-1)