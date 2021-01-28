class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n
        for index in range(len(res)-1,-1,-1):
            if k <= 25:
                res[index] = chr(97+k)
                break
            else:
                res[index] = 'z'
                k -= 25
        newStr = ""
        for c in res:
            newStr += c
        return newStr
            
                