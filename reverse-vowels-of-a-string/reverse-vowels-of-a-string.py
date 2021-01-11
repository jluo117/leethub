class Solution:
    def reverseVowels(self, s: str) -> str:
        L = 0
        R = len(s)-1
        tmpAry = []
        for c in s:
            tmpAry.append(c)
        vowes = {'a','A','e','E','i','I','o','O','u','U'}
        while L < R:
            if tmpAry[L] in vowes and tmpAry[R] in vowes:
                tmpAry[L],tmpAry[R] = tmpAry[R],tmpAry[L]
                L += 1
                R -= 1
                continue
            if tmpAry[L] not in vowes:
                L += 1
            if tmpAry[R] not in vowes:
                R -= 1
        newStr = ""
        for c in tmpAry:
            newStr += c
        return newStr
        
        
