class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        table = {}
        L = 0
        R = len(s)-1
        def helper(L,R):
            if (L,R) in table:
                return table[(L,R)]
            if L >= len(s) and R <= -1:
                return 0
            
            min_cost = float('inf')
            if L < len(s) and R > -1:
                if s[L] == s[R]:
                    min_cost = min(min_cost,helper(L+1,R-1))
                else:
                    min_cost = min(min_cost,helper(L+1,R-1)+2)
            if L < len(s):
                min_cost = min(min_cost,helper(L+1,R)+1)
            if R >= 0:
                min_cost = min(min_cost,helper(L,R-1)+1)
            table[(L,R)] = min_cost
            return min_cost
        res =  helper(L,R)
        return res//2 <= k