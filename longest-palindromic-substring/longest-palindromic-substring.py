class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        longest = 0
        maxL = 0
        maxR = 0
        for index in range(1,len(s)):
            if s[index -1] == s[index]:
                    L = index - 1
                    R = index
                    while s[L] == s[R]:
                        L-=1
                        R+=1
                        if L == -1 or R == len(s):
                            break
                    L+=1
                    R -= 1
                    print(R + L + 1)
                    if longest < R - L + 1:
                        
                        maxL = L
                        maxR = R
                        longest = R - L + 1
            if index == len(s) -1:
                break
            if s[index -1] == s[index + 1]:
                L = index -1
                R = index + 1
                while s[L] == s[R]:
                    L -= 1
                    R += 1
                    if L == -1 or R == len(s):
                        break
                L +=1
                R -=1
                print(R - L + 1)
                if longest < R - L + 1:
                    maxL = L
                    maxR = R
                    longest = R - L + 1
                    
        res = ""
        for index in range(maxL,maxR + 1):
            res += s[index]
        return res
                        
                    
