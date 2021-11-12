class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        index = len(nums)-2
        while index >= 0 and nums[index+1] <= nums[index]:
            index -= 1
        if index >= 0:
            end_point = len(nums)-1
            while end_point >= 0 and nums[end_point] <= nums[index]:
                end_point -= 1
            nums[end_point],nums[index] = nums[index],nums[end_point]
        end_point = len(nums)-1
        index += 1
        while index < end_point:
            nums[end_point],nums[index] = nums[index],nums[end_point]
            end_point -= 1
            index += 1
        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        