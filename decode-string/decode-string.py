class Solution:
    def decodeString(self, s: str) -> str:
        self.index = 0
        def helper():
            curStr = ""
            while self.index < len(s):
                if '0' <= s[self.index] <= '9':
                    numStr = ""
                    while '0' <= s[self.index] <= '9':
                        numStr += s[self.index]
                        self.index += 1
                    self.index += 1
                    curStr += helper() * int(numStr)
                else:
                    if s[self.index] == ']':
                        self.index += 1
                        return curStr
                    curStr += s[self.index]
                    self.index += 1
            return curStr
        res = ""
        while self.index < len(s):
            res += helper()
        return res