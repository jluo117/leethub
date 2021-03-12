class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.Counter()
        def isValid():
            tol = 0
            maxVal = 0
            for val in freq:
                maxVal = max(maxVal,freq[val])
                tol += freq[val]
            return tol - maxVal <= k
        L = 0 
        R = 0
        maxSize = 0
        while R < len(s):
            freq[s[R]] += 1
            while not isValid():
                freq[s[L]] -= 1
                L += 1
            maxSize = max(maxSize,(R-L)+1)
            R += 1
        return maxSize