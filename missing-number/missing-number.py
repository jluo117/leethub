class Solution:
    def missingNumber(self, nums):
        zeroFlip = False
        over = False
        for num in nums:
            targetIndex = abs(num)
            if targetIndex >= len(nums):
                over = True
                continue
            if nums[targetIndex] == 0:
                zeroFlip = True
            nums[targetIndex] *= -1
        for index in range(len(nums)):
            if nums[index] > 0:
                return index
            if nums[index] == 0 and zeroFlip == False:
                return index
        return len(nums)
            
                
        """
        :type nums: List[int]
        :rtype: int
        """
        