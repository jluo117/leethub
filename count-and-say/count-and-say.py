class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prevStr = self.countAndSay(n-1)
        
        prevVal = ""
        count = 0
        res = []
        for c in prevStr:
            if prevVal == "":
                prevVal = c
                count = 1
                continue
            if prevVal != c:
                res.append((prevVal,count))
                prevVal = c
                count = 1
                continue
            count += 1
        res.append((prevVal,count))
        newStr = ""
        for val in res:
            newStr +=  str(val[1]) + val[0]
        return newStr
        