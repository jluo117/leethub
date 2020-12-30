class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        runningMax = -float(inf)
        runningSum = 0
        for num in nums:
            if runningSum + num < num:
                runningSum = num
            else:
                runningSum += num
            runningMax = max(runningSum,runningMax)
        return runningMax
        
