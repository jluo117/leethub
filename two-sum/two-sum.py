class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenVal = {}
        for index , num in enumerate(nums):
            targetVal = target - num
            if targetVal in seenVal:
                return seenVal[targetVal],index
            seenVal[num] = index
        
        