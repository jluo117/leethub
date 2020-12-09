class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        runningIndex = []
        for digit in digits:
            if len(runningIndex) == 0:
                for c in table[digit]:
                    runningIndex.append(c)
                continue
            newRow = []
            for curChar in runningIndex:
                for c in table[digit]:
                    newRow.append(curChar+c)
            runningIndex = newRow
        return runningIndex
        
