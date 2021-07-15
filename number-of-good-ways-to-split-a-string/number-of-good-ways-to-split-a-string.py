class Solution:
    def numSplits(self, s: str) -> int:
            
        setB = collections.Counter(s)
        setA = collections.Counter()
        pos = 0
        for c in s:
            setB[c] -= 1
            if setB[c] == 0:
                del setB[c]
            setA[c] += 1
            pos += len(setA) == len(setB)
        return pos
            
        