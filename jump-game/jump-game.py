class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastTrue = len(nums)-1
        for index in range(len(nums)-1,-1,-1):
            if nums[index] + index >= lastTrue:
                lastTrue = index
        return lastTrue == 0