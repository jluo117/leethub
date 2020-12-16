class Solution:
    def maximumSwap(self, num: int) -> int:
        maxNum = num
        numStr = str(num)
        numAry = []
        for c in numStr:
            numAry.append(c)
        def stringThem(ary):
            CurStr = ""
            for c in ary:
                CurStr += c
            return int(CurStr)
        for l in range(len(numAry)):
            for r in range(l+1,len(numAry)):
                numAry[l],numAry[r] = numAry[r],numAry[l]
                
                maxNum = max(maxNum,stringThem(numAry))
                numAry[l],numAry[r] = numAry[r],numAry[l]
        return maxNum
        
