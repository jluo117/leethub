class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        toMerge = []
        res = []
        for interval in intervals:
            toMerge.append((interval[0],False))
            toMerge.append((interval[1],True))
        bisect.insort(toMerge,(newInterval[0],False))
        bisect.insort(toMerge,(newInterval[1],True))
        curStart = -1
        depth = 0
        for sec in toMerge:
            if sec[1] == False:
                depth += 1
                if curStart == -1:
                    curStart = sec[0]
            else:
                depth -= 1
                if depth == 0:
                    res.append((curStart,sec[0]))
                    curStart = -1
        return res
                
                
        
