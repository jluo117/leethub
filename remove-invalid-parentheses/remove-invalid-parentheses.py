class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        table = {}
        def helper(index,depth,curPath,moves):
            if index == len(s):
                if depth == 0:
                    if moves not in table:
                        table[moves] = {curPath}
                    else:
                        table[moves].add(curPath)
                return
            if s[index] == '(':
                helper(index+1,depth+1,curPath+'(',moves)
                helper(index+1,depth,curPath,moves+1)
            elif s[index] == ')':
                if depth:
                    helper(index+1,depth-1,curPath+')',moves)
                    helper(index+1,depth,curPath,moves+1)
                else:
                    helper(index+1,depth,curPath,moves+1)
            else:
                helper(index+1,depth,curPath+ s[index],moves)
        helper(0,0,"",0)
        minVal = min(table)
        res = []
        for val in table[minVal]:
            res.append(val)
        return res
        
