class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            pos = []
            curNum = 1
            while n > 0:
                pos.append(curNum)
                pos.append(-curNum)
                curNum += 1
                n -= 2
            return pos
        else:
            pos = [0]
            n -= 1
            curNum = 1
            while n > 0:
                pos.append(curNum)
                pos.append(-curNum)
                curNum += 1
                n -= 2
            return pos
                
        
