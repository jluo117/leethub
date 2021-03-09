class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hist = collections.Counter([0])
        runningSum = 0
        tol = 0
        for num in nums:
            runningSum += num
            if runningSum - k in hist:
                tol += hist[runningSum-k]
            
            hist[runningSum] += 1
           
        return tol
        
        