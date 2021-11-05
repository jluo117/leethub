class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        R = 0
        running_sum = 0
        min_size = float('inf')
        while R < len(nums):
            running_sum += nums[R]
            while running_sum >= target:
                min_size = min((R-L)+1,min_size)
                running_sum -= nums[L]
                L += 1
            R += 1
        if min_size == float('inf'):
            return 0
        return min_size
            