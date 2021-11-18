class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            targetNum = abs(num)
            if targetNum <= len(nums):
                targetNum -= 1
                if nums[targetNum] < 0:
                    continue
                nums[targetNum] = -nums[targetNum]
        
        
        res = []
        for index in range(len(nums)):
            if nums[index] > 0:
                res.append(index+1)
        return res
        