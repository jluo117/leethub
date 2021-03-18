class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        def helper(num):
            if num in table:
                return table[num]
            res = 1
            if num + 1 in nums:
                res += helper(num+1)
                table[num] = res
                return res
            table[num] = res
            return res
        maxVal = 0
        for num in nums:
            maxVal = max(maxVal,helper(num))
        return maxVal
        