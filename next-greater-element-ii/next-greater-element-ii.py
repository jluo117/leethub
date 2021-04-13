'''
[1,2,1]
'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        curStk = []
        for index in range(len(nums)-1,-1,-1):
            curStk.append((index,nums[index]))
        res = [-1] * len(nums)
        for index in range(len(nums)-1,-1,-1):
            while len(curStk) and curStk[-1][1] <= nums[index]:
                curStk.pop()
            if len(curStk) == 0:
                res[index] = -1
            else:
                res[index] = curStk[-1][1]
            curStk.append((index,nums[index]))
        return res
                