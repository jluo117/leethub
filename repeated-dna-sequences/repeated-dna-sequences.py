from collections import Counter
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        valCounts = Counter()
        curStr = ""
        for c in s:
            curStr += c
            if len(curStr) > 10:
                curStr = curStr[1:]
            if len(curStr) == 10:
                valCounts[curStr] += 1
        for val in valCounts:
            if valCounts[val] > 1:
                res.append(val)
        return res
                
        