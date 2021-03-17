class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        def helper(num):
            if num in table:
                return table[num]
            longest = 1
            if num+1 in nums:
                longest += helper(num+1)
            table[num] = longest
            return longest
        res = 0
        for num in nums:
            
            res = max(res,helper(num))
        return res