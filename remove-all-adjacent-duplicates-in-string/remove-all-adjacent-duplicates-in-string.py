class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = []
        for c in S:
            if len(stk) == 0:
                stk.append(c)
                continue
            if stk[-1] != c:
                stk.append(c)
                continue
            stk.pop()
        res = ""
        for c in stk:
            res += c
        return res
        