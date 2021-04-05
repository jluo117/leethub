class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            targetIndex = abs(num) -1
            if nums[targetIndex] < 0:
                return abs(num)
            nums[targetIndex] *= -1
        return len(nums)+1
        