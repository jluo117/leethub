class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        freq = [0] * len(nums)
        def findBiggest(index):
            startNum = nums[index]
            maxLen = 0
            curFreq = 0
            for upper in range(index+1,len(nums)):
                if nums[upper] > startNum:
                    if dp[upper] > maxLen:
                        curFreq = freq[upper]
                        maxLen = dp[upper]
                    elif dp[upper] == maxLen:
                        curFreq += freq[upper]
            if maxLen == 0:
                dp[index] = 1
                freq[index] = 1
                
            else:
                dp[index] = maxLen + 1
                freq[index] = curFreq
            
            return 
        maxVal = 0
        for R in range(len(nums)-1,-1,-1):
            findBiggest(R)
        maxTimes = 0
        
        for long,times in zip(dp,freq):
            if long > maxVal:
                maxTimes = times
                maxVal = long
            elif long == maxVal:
                maxTimes += times
        return maxTimes