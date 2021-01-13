'''
abca
​
​
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1
        def helper(L,R):
            while L <= R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True
        while L <= R:
            if s[L] != s[R]:
                return helper(L+1,R) or helper(L,R-1)
            L += 1
            R -= 1
        return True
            
        
