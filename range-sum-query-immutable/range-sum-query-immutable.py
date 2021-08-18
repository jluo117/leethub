class NumArray:

    def __init__(self, nums: List[int]):
        self.runningSum = []
        curSum = 0
        for num in nums:
            curSum += num
            self.runningSum.append(curSum)
        

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.runningSum[j]
        return self.runningSum[j] - self.runningSum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)