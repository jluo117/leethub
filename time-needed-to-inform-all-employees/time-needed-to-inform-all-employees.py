class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0
        managers = {}
        for index in range(n):
            curMan = manager[index]
            
            if curMan == -1:
                continue
            if curMan in managers:
                managers[curMan].append(index)
            else:
                managers[curMan] = [index]
        def helper(curID):
            if curID not in managers:
                return 0
            maxTime = 0
            for val in managers[curID]:
                maxTime = max(maxTime,helper(val)+informTime[curID])
            return maxTime
        return helper(headID)
            
        
