class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        need = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0:
                    need += 1
                else:
                    count -= 1
        return need + count
                    