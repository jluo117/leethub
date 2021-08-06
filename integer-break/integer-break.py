class Solution:
    def integerBreak(self, n: int) -> int:
        table = {}
        def helper(rem):
            if (rem) in table:
                return table[rem]
            if rem == 0:
                return 1
            if rem < 0:
                return -1
            maxRes = 0
            for i in range(1,rem+1):
                maxRes = max(maxRes,helper(rem-i)*i)
            table[(rem)] = maxRes
            return maxRes
        
        maxRes = 0 
        for i in range(1,n):
            maxRes = max(helper(n-i)*i,maxRes)
        return maxRes
            