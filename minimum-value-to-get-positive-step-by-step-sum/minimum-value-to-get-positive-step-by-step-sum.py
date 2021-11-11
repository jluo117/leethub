class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        running_sum = 0
        min_val = float('inf')
        for num in nums:
            running_sum += num
            min_val = min(min_val,running_sum)
        if min_val > 0:
            return 1
        return abs(min_val) + 1