class Solution:
    def customSortString(self, S: str, T: str) -> str:
        table = {}
        for index in range(len(S)):
            table[S[index]] = index
            
        sortAry = []
        for c in T:
            if c not in table:
                sortAry.append((len(table),c))
            else:
                sortAry.append((table[c],c))
        sortAry.sort()
        res = ""
        for c in sortAry:
            res += c[1]
        return res
        
