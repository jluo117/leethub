​
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        resStr = ""
        carryOver = 0
        L = len(num1)-1
        R = len(num2) -1
        while L >= 0 or R >= 0:
            if L == -1:
                resInt = int(num2[R]) + carryOver
                
                if resInt >= 10:
                    carryOver = 1
                    resInt -= 10
                else:
                    carryOver = 0
                resStr += str(resInt)
                R -= 1
            elif R == -1:
                resInt = int(num1[L]) + carryOver
                
                if resInt >= 10:
                    carryOver = 1
                    resInt -= 10
                else:
                    carryOver = 0
                resStr += str(resInt)
                L -= 1
            else:
                resInt = int(num1[L]) + int(num2[R]) + carryOver
                if resInt >= 10:
                    carryOver = 1
                    resInt -= 10
                else:
                    carryOver = 0
                resStr += str(resInt)
                L -= 1
                R -= 1
        if carryOver > 0:
            resStr += str(carryOver)
        
        return resStr[::-1]
