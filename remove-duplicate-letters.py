class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        table = {}
        for c in s:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        stk = []
        used = set()
        for c in s:
            if c in used:
                table[c] -= 1
                continue
            if len(stk) == 0:
                stk.append(c)
                used.add(c)
                continue
            while len(stk) > 0 and stk[-1] > c:
                if table[stk[-1]] == 1:
                    break
                table[stk[-1]] -= 1
                used.remove(stk[-1])
                stk.pop()
            stk.append(c)
            used.add(c)
        res = ""
        for c in stk:
            res += c
        return res
