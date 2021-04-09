class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hist = {0:-1}
        runningSum = 0
        if nums == [0]:
            return False
        for index in range(len(nums)):
            num = nums[index]
            runningSum += num
            if runningSum % k in hist:
                if index - hist[runningSum%k] >= 2:
                    return True
            else:
                hist[runningSum%k] = index
        return False