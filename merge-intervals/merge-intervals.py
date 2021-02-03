class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ending = None
        start = None
        if len(intervals) == 0:
            return []
        res = []
        for interval in intervals:
            if start == None:
                start = interval[0]
                ending = interval[1]
                continue
            if ending >= interval[0]:
                ending = max(interval[1],ending)
            else:
                res.append([start,ending])
                start = interval[0]
                ending = interval[1]
        res.append([start,ending])
        return res
        
        