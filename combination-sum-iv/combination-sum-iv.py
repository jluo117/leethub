'''
​
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        table = {}
        def helper(curNum):
            if curNum == 0:
                return 1
            if curNum in table:
                return table[curNum]
            pos = 0
            for num in nums:
                if curNum - num >= 0:
                    pos += helper(curNum-num)
            table[curNum] = pos
            return pos
        return helper(target)
