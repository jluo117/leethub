class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = -float('inf')
        for num in nums:
            tmp =curMax
            curMax = max(curMax*num,curMin*num,num)
            curMin = min(tmp*num,curMin*num,num)
            res = max(curMax,res)
        return res
        