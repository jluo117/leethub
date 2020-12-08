class Solution:
    def maxLength(self, arr: List[str]) -> int:
        hashAry = []
        for word in arr:
            valid = True
            curTable = set()
            for c in word:
                if c in curTable:
                    valid = False
                    break
                else:
                    curTable.add(c)
            if valid:
                hashAry.append((curTable,len(word)))
        table = {}
        def helper(inUsed,index):
            
            if index == len(hashAry):
                return 0
            if (inUsed,index) in table:
                return table[(inUsed,index)]
            for c in hashAry[index][0]:
                if c in inUsed:
                    res = helper(inUsed,index+1)
                    table[(inUsed,index)] = res
                    return res
            toAppend = ""
            for c in hashAry[index][0]:
                toAppend += c
            toAppend += inUsed
            res = max(helper(inUsed,index+1),helper("".join(sorted(toAppend)),index+1) + hashAry[index][1])
            table[(inUsed,index)] = res
            return res
        return helper("",0)
    
                
            
        
