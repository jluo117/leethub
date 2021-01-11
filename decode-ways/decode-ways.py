class Solution:
    def numDecodings(self, s: str) -> int:
        table = {}
        def helper(index):
            if index == len(s):
                return 1
            if index in table:
                return table[index]
            pos = 0
            if s[index] == '0':
                return 0
            if index +2 <= len(s):
                checkNum = int(s[index] + s[index+1])
                if checkNum < 27:
                    pos += helper(index+2)
            pos += helper(index+1)
            table[index] = pos
            return pos
        return helper(0)
