class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        nums.sort()
        maxVal = nums[-1] * nums[-2] * nums[-3]
        if nums[-1] >= 0:
            negative = nums[0] * nums[1] * nums[-1]
            return max(maxVal,negative)
        return maxVal
        
