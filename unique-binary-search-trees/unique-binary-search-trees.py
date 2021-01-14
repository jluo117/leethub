class Solution:
    def numTrees(self, n: int) -> int:
        table = {}
        def helper(n):
            if n == 1 or n == 0:
                return 1
            if n in table:
                return table[n]
            
            pos = 0
            for i in range(1,n+1):
                pos += (helper(i-1) * helper(n-i))
            table[n] = pos
            return pos
        return helper(n)
        
