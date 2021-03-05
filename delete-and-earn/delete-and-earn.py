class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        houses = []
        table = collections.Counter(nums)
        for val in table:
            houses.append((val,table[val]))
        houses.sort()
        dp = {}
        def helper(canRob,index):
            if (index,canRob) in dp:
                return dp[(index,canRob)]
            if index == len(houses):
                return 0
            if canRob:
                res = helper(True,index+1)
                if index+ 1 < len(houses) and houses[index+1][0] == houses[index][0]+1:
                    res = max(helper(False,index+1)+(houses[index][0]*houses[index][1]),res)
                else:
                    res = max(helper(True,index+1)+(houses[index][0]*houses[index][1]),res)
                dp[(index,canRob)] = res
                return res
            res = helper(True,index+1)
            dp[(index,canRob)] = res
            return res
        return helper(-1,0)