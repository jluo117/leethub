class Solution:
    def rob(self, nums: List[int]) -> int:
        table = {}
        def helper(index,canRob):
            if index == len(nums):
                return 0
            if canRob == False:
                return helper(index+1,True)
            if index in table:
                return table[index]
            res = max(helper(index+1,True),helper(index+1,False)+nums[index])
            table[index] = res
            return res
        return helper(0,True)
                
        
