class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        while L <= R:
            if L == R:
                return R
            mid_point = (L + R) // 2
            if mid_point -1 >= 0 and mid_point + 1 < len(nums):
                if nums[mid_point] > nums[mid_point-1] and nums[mid_point] > nums[mid_point+1]:
                    return mid_point
            if nums[mid_point + 1] > nums[mid_point]:
                L = mid_point + 1
            else:
                R = mid_point - 1
        return L
        