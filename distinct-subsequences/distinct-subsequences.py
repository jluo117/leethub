class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        table = {}
        def helper(sIndex,tIndex):
            if (sIndex,tIndex) in table:
                return table[(sIndex,tIndex)]
            if len(t) == tIndex:
                return 1
            if len(s) == sIndex:
                return 0
            pos = 0
            if s[sIndex] == t[tIndex]:
                pos += helper(sIndex+1,tIndex+1)
            pos += helper(sIndex+1,tIndex)
            table[(sIndex,tIndex)] = pos
            return pos
        return helper(0,0)
