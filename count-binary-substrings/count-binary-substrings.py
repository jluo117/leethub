class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def expand(index):
            if index < 1:
                return 0
            Lindex = index-1
            curIndex = index
            count = 0
            Ltarget = s[index-1]
            Rtarget = s[index]
            if Ltarget == Rtarget:
                return 0
            while Lindex >= 0 and curIndex < len(s):
                if Ltarget != s[Lindex] or Rtarget != s[curIndex]:
                    return count
                count += 1
                Lindex -= 1
                curIndex += 1
                
            return count
        count = 0
        for index in range(len(s)):
            count += expand(index)
        return count
        