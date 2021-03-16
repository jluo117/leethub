class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxProduct = nums[0]
        minProduct = nums[0]
        maxVal = maxProduct
        for index in range(1,len(nums)):
            num = nums[index]
            tmp = maxProduct
            maxProduct = max(maxProduct*num,minProduct*num,num)
            minProduct = min(minProduct*num,tmp*num,num)
            maxVal = max(maxVal,maxProduct)
        return maxVal
            
        