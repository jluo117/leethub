'4^4 -> 4^2 * 4^2'
class Solution:
    def myPow(self, x: float, n: int) -> float:
        table = {}
        def helper(n):
            if n in table:
                return table[n]
            if n == 1:
                return x
            if n % 2 == 1:
                res = helper(n-1) * x
                table[n] = res
                return res
            else:
                res = helper(n/2) * helper(n/2)
                table[n] = res
                return res
        if n == 0:
            return 1
        if n < 0:
            res = helper(abs(n))
            return 1/res
        return helper(n)
        
        
            
        