class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if len(stk) == 0:
                stk.append([c,1])
                continue
            if stk[-1][0] == c:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append([c,1])
        res = ""
        for val in stk:
            res += val[0] * val[1]
        return res
        