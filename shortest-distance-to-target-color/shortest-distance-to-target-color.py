class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        Ldis = [-1,-1,-1]
        ary = []
        for index in range(len(colors)):
            indexColor = colors[index]
            Ldis[indexColor-1] = index
            newAry = []
            for v in Ldis:
                if v == -1:
                    newAry.append(-1)
                    continue
                newAry.append(abs(index - v))
            ary.append(newAry)
        
        
        Rdis = [-1,-1,-1]
        for index in range(len(colors)-1,-1,-1):
            indexColor = colors[index]
            Rdis[indexColor-1] = index
            newAry = []
            for v in Rdis:
                if v == -1:
                    newAry.append(-1)
                    continue
                newAry.append(abs(index-v))
            
            for cIndex in range(len(ary[index])):
                if newAry[cIndex] == -1:
                    continue
                if ary[index][cIndex] == -1:
                    ary[index][cIndex] = newAry[cIndex]
                    continue
                ary[index][cIndex] = min(ary[index][cIndex],newAry[cIndex])
        
        res = []
        for querie in queries:
            index = querie[0]
            targetCol = querie[1] -1
            res.append(ary[index][targetCol])
        return res
        
            
            
        