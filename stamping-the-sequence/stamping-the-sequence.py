'''
aabcaca
a****ca
****ca

'''
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if stamp not in target:
            return []
        strAry = []
        for c in target:
            strAry.append(c)
        def isMatch(curAry):
            for i,j in zip(curAry,stamp):
                if i == '*':
                    continue
                if i != j:
                    return False
            return True
        def allStars(checkAry):
            for val in checkAry:
                if val != '*':
                    return False
            return True
        res = []
        while not allStars(strAry):
            curAry = deque()
            
            R = 0
            while R < len(target):
                curAry.append(strAry[R])
                if len(curAry) > len(stamp):
                    curAry.popleft()
                if len(curAry) == len(stamp):
                    if allStars(curAry) == False:
                        if isMatch(curAry):
                            res.append((R-len(stamp)+1))
                            for i in range((R-len(stamp))+1,R+1):
                                strAry[i] = '*'
                            break
            
                R+=1
            if R == len(target):
                return []
        L = 0
        R = len(res)-1
        while L < R:
            res[R],res[L] = res[L],res[R]
            L += 1
            R -= 1
        return res
                                          
                            