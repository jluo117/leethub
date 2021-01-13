class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        longest = 0
        seenVal = set()
        for Lindex in range(len(S)):
            curStr = S[Lindex]
            if curStr in seenVal:
                longest = max(longest,len(curStr))
            seenVal.add(curStr)
            for Rindex in range(Lindex+1,len(S)):
                curStr += S[Rindex]
                if curStr in seenVal:
                    longest = max(longest,len(curStr))
                seenVal.add(curStr)
        return longest
                
