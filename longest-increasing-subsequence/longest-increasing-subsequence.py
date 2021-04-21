class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = {}
        def helper(index):
            if index in table:
                return table[index]
            if index == len(nums):
                return 0
            
            maxSize = 1
            for checkIndex in range(index+1,len(nums)):
                if nums[checkIndex] > nums[index]:
                    maxSize = max(maxSize,helper(checkIndex)+1)
            table[index] = maxSize
            return maxSize
        res = 0
        for index in range(len(nums)):
            res = max(helper(index),res)
        return res