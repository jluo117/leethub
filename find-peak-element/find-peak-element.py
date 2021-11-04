class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def helper(L,R):
            if L == R:
                return R
            mid_point = (L+R)//2
            if L + 1 == R:
                if nums[L] > nums[R]:
                    return L
                else:
                    return R
            if nums[mid_point-1] < nums[mid_point] > nums[mid_point+1]:
                return mid_point
            if nums[mid_point] < nums[mid_point+1]:
                return helper(mid_point+1,R)
            else:
                return helper(L,mid_point-1)
        return helper(0,len(nums)-1)
                