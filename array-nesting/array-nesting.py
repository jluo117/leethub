class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visitSet = set()
        def helper(index):
            if index in visitSet or index >= len(nums):
                return 0
            visitSet.add(index)
            res = helper(nums[index])+1
            return res
        maxVal = 0
        for index in range(len(nums)):
            maxVal = max(maxVal,helper(index))
        return maxVal
