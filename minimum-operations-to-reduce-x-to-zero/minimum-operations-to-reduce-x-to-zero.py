class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        arySum = sum(nums)
        L = 0
        R = 0
        targetSum = arySum - x
        curSum = 0
        minDis = float('inf')
        while R < len(nums):
            curSum += nums[R]
            while L <=R and curSum > targetSum:
                curSum -= nums[L]
                L += 1
            if curSum == targetSum:
                curDis = len(nums)- ((R-L) + 1)
                minDis = min(minDis,curDis)
            
            R += 1
        if minDis == float('inf'):
            return -1
        return minDis
        
