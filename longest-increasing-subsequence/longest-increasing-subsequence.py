
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        for index in range(len(nums)-1,-1,-1):
            maxVal = 1
            for lowerIndex in range(index+1,len(nums)):
                if nums[lowerIndex] > nums[index]:
                    maxVal = max(dp[lowerIndex]+1,maxVal)
            dp[index] = maxVal
        maxVal = 0
        for val in dp:
            maxVal = max(maxVal,dp[val])
        return maxVal
            
