class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetDict = collections.Counter(t)
        curDic = collections.Counter()
        def checkMatch():
            for val in targetDict:
                if val not in curDic:
                    return False
                if targetDict[val] > curDic[val]:
                    return False
            return True
        L =0
        R = 0
        minWindow = [-float('inf'),float('inf')]
        while R < len(s):
            curDic[s[R]] += 1
            while checkMatch():
                if (R-L)+1 < (minWindow[1] - minWindow[0]) +1:
                    minWindow = [L,R]
                curDic[s[L]] -= 1
                L += 1
            R += 1
        res = ""
        if minWindow[0] == -float('inf'):
            return ""
        for i in range(minWindow[0],minWindow[1]+1):
            res += s[i]
        return res
        
        