'''
aba -> aba 
baab -> 2 a/a b/b
​
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        pos = 0
        for index in range(len(s)):
            L = index
            R = index
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    pos += 1
                else:
                    break
                L -= 1
                R += 1
            if index >= 1:
                if s[index-1] == s[index]:
                    L = index-1
                    R = index
                    while L >= 0 and R <len(s):
                        if s[L] == s[R]:
                            pos += 1
                        
                        else:
                            break
                        L -= 1
                        R += 1
        return pos
        
