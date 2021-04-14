class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        numCount = collections.Counter(nums)
        ary = [i for i in numCount]
        ary.sort()
        dp = {}
        def helper(index):
            if index in dp:
                return dp[index]
            if index >= len(ary):
                return 0
            take = numCount[ary[index]] * ary[index]
            maxVal = 0
            if index + 1 == len(ary):
                return take
            if ary[index+1]  == ary[index]+1:
                
                maxVal = max(helper(index+2) + take,helper(index+1))
            else:
                maxVal = take + helper(index+1)
            dp[index] = maxVal
            return maxVal
        return helper(0)
            
            