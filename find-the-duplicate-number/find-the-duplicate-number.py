class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            index = abs(i)
            if nums[index] < 0:
                return index
            nums[index] *= -1
        return len(nums)
        