class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        takenWords = set()
        wordMap = {}
        if len(s) != len(t):
            return False
        for c1,c2 in zip(s,t):
            if c1 in wordMap:
                if c2 != wordMap[c1]:
                    return False
            else:
                wordMap[c1] = c2
                if c2 in takenWords:
                    return False
                takenWords.add(c2)
        return True
            
        