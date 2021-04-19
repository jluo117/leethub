class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        seenVals = collections.Counter()
        L = 0
        while L < len(s):
            curStr = ""
            curSet = set()
            for curIndex in range(L,min(L+maxSize,len(s))):
                curSet.add(s[curIndex])
                curStr += s[curIndex]
                if len(curSet) > maxLetters:
                    break
                if (curIndex-L) + 1 >= minSize:
                    seenVals[curStr] += 1
            L += 1
        if len(seenVals) == 0:
            return 0
        maxVal = max([seenVals[val] for val in seenVals])
        return maxVal