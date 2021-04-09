class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        activeSet = set()
        charCounter = collections.Counter()
        L = 0
        R = 0
        maxSize = 0
        while R < len(s):
            activeSet.add(s[R])
            charCounter[s[R]] += 1
            while len(activeSet) > k:
                charCounter[s[L]] -= 1
                if charCounter[s[L]] == 0:
                    activeSet.remove(s[L])
                L += 1
            maxSize = max(maxSize,((R-L)+1))
            R += 1
        return maxSize
                