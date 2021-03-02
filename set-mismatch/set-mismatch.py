class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        extra = None
        for num in nums:
            curIndex = abs(num)-1
            
            if nums[curIndex] < 0:
                extra = abs(num)
            else:
                nums[curIndex] *= -1
       
        for index in range(len(nums)):
            if nums[index] > 0:
                return [extra,index+1]
        
        