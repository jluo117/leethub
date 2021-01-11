class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        over = set()
        for c in range(len(s)):
            if s[c] == '(':
                stk.append(c)
            if s[c] == ')':
                if len(stk) == 0:
                    over.add(c)
                else:
                    stk.pop()
        
        res = ""
        for val in stk:
            over.add(val)
        for c in range(len(s)):
            if c in over:
                continue
            else:
                res += s[c]
        return res
        
