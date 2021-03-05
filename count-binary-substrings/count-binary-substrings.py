class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = None
        curCount = 0
        prevCount = 0
        pos = 0
        for c in s:
            if prev == None:
                prev = c
            if prev == c:
                curCount += 1
            elif prev != c:
                prevCount = curCount
                curCount = 1
                prev = c
            if prevCount >= curCount:
                pos += 1
        return pos
        