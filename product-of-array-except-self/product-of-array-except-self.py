class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        runningProduct = []
        curProduct = 1
        if len(nums) == 0:
            return []
        for num in nums:
            runningProduct.append(num*curProduct)
            curProduct = runningProduct[-1]
        curProduct = 1
        for index in range(len(nums)-1,-1,-1):
            nums[index] = curProduct * nums[index]
            curProduct = nums[index]
        prev = 1
        for index in range(len(runningProduct)):
            tmp = runningProduct[index]
            if index < len(nums)-1:
                runningProduct[index] = prev * nums[index+1] 
            else:
                runningProduct[index] = prev
            prev = tmp
        return runningProduct
        