class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        table = {}
        def helper(index,rem):
            if index == len(jobDifficulty) and rem == 0:
                return 0
            if rem == 0 or index == len(jobDifficulty):
                return float('inf')
            if (index,rem) in table:
                return table[(index,rem)]
            minWork = float('inf')
            minTask = 0
            for Iindex in range(index,len(jobDifficulty)):
                minTask = max(minTask,jobDifficulty[Iindex])
                minWork = min(helper(Iindex+1,rem-1) + minTask,minWork)
            table[(index,rem)] = minWork
            return minWork
        res = helper(0,d)
        if res == float('inf'):
            return -1
        return res
        
