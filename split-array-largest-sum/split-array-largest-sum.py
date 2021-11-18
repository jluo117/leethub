class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isPos(targetNum):
            tolM = 0
            curSum = 0
            highestNum = 0
            for num in nums:
                if curSum + num > targetNum:
                    tolM += 1
                    curSum = num
                else:
                    curSum += num
            if curSum > 0:
                tolM += 1
            return tolM <= m
        maxAry = sum(nums)
        minAry = max(nums)
        smallest = float('inf')
        while minAry <= maxAry:
            middle = (minAry + maxAry)//2
            if isPos(middle):
                smallest = middle
                maxAry = middle - 1
            else:
                minAry = middle + 1
        return smallest
    
                
                