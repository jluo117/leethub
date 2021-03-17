class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit)))
        
        @cache
        def fn(i): 
            """Return max profit starting from index i."""
            if i == len(startTime): return 0 
            ii = bisect_left(startTime, endTime[i])
            return max(fn(i+1), profit[i] + fn(ii))
        
        return fn(0)