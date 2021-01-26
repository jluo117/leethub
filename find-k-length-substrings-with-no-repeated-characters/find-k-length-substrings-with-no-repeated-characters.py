class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        L = 0
        R = 0
        inSet = set()
        count = 0
        while R < len(S):
            while S[R] in inSet:
                inSet.remove(S[L])
                L += 1
            inSet.add(S[R])
            if (R-L)+1 == K:
                count += 1
                inSet.remove(S[L])
                L += 1
            R += 1
        return count
        
