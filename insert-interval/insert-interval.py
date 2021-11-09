class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals,newInterval)
        print(intervals)
        cur_end = None
        cur_start = None
        res = []
        for interval in intervals:
            if cur_end == None:
                cur_start = interval[0]
                cur_end = interval[1]
                continue
            if cur_end < interval[0]:
                res.append([cur_start,cur_end])
                cur_start = interval[0]
                cur_end = interval[1]
            else:
                cur_end = max(interval[1],cur_end)
        res.append([cur_start,cur_end])
        return res
            
                
                
        