class Solution:
    def minSwaps(self, s: str) -> int:
        stk = 0
        needed = 0
        for c in s:
            if c == ']':
                if stk == 0:
                    needed += 1
                else:
                    stk -= 1
            else:
                stk += 1
        needed += stk
        needed /= 2
        if needed == 1:
            return 1
        else:
            return math.ceil(needed / 2)
        
        