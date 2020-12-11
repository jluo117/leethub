class Solution:
    def findContestMatch(self, n: int) -> str:
        L = 1
        R = n
        res = []
        curRound = 0
        while L < R:
            strRes = '('+str(L)+','+str(R)+')'
            res.append(strRes)
            L += 1
            R -= 1
        
        curRound += 1
        while pow(2,curRound) < n:
            newRes = []
            L = 0
            R = len(res) -1
            while L < R:
                newStr = "(" + res[L] + ',' + res[R] + ')'
                newRes.append(newStr)
                L += 1
                R -= 1
            res = newRes
            curRound += 1
        return res[0]
        
