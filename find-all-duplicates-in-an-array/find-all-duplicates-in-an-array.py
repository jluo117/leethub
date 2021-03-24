class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for index in range(len(nums)):
            targetIndex = abs(nums[index])-1
            if nums[targetIndex] < 0:
                res.append(abs(nums[index]))
            else:
                nums[targetIndex] *= -1
        return res
        