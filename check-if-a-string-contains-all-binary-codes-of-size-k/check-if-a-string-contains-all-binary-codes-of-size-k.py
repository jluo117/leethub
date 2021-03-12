class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seenVal = set()
        L = 0
        R = 0
        curVal = 0
        while R < len(s):
            if s[R] == '1':
                curVal *= 2
                curVal += 1
            else:
                curVal *= 2
            
            if (R-L)+1 == k:
                seenVal.add(curVal)
                
                if s[L] == '1':
                    curVal -= ((2 ** (k-1)))
            
                L += 1
            R += 1
        
        return len(seenVal) == 2 ** k