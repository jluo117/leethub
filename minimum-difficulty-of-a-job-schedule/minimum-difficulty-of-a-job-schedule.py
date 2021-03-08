class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        table = {}
        def helper(index,day):
            if (index,day) in table:
                return table[(index,day)]
            if day==0 and index == len(jobDifficulty):
                return 0
            if index == len(jobDifficulty) and day > 0:
                return float('inf')
            if day == 0 and index != len(jobDifficulty):
                return float('inf')
            
            
            curMax = 0
            res = float('inf')
            for curIndex in range(index,len(jobDifficulty)):
                curMax = max(curMax,jobDifficulty[curIndex])
                res = min(curMax+helper(curIndex+1,day-1),res)
            table[(index,day)] = res
            return res
        res = helper(0,d)
        if res == float('inf'):
            return -1
        return res
                
        