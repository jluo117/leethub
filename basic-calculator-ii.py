class Solution:
    def calculate(self, s: str) -> int:
        clean = []
        cIndex = 0
        while cIndex < len(s):
            if s[cIndex] == ' ':
                cIndex += 1
                continue
            if s[cIndex] in {'1','2','3','4','5','6','7','8','9','0'}:
                curNum = ''
                while cIndex < len(s) and s[cIndex] in {'1','2','3','4','5','6','7','8','9','0'}:
                    curNum += s[cIndex]
                    cIndex += 1
                clean.append(curNum)
            else:
                clean.append(s[cIndex])
                cIndex += 1
        
                
                    
            
        stk = []
        index = 0
        while index < len(clean):
            c = clean[index]
            if c == '*' or c == '/':
                popVal = stk.pop()
                if c == '*':
                    stk.append(int(popVal) * int(clean[index+1]))
                else:
                    stk.append(int(popVal)// int(clean[index+1]))
                index += 2
            else:
                stk.append(c)
                index += 1
        index = 0
        curVal = 0
        while index < len(stk):
            if index == 0:
                curVal = int(stk[index])
                index += 1
            elif stk[index] == '+' or stk[index] == '-':
                if stk[index] == '+':
                    curVal = curVal + int(stk[index+1])
                else:
                    curVal = curVal - int(stk[index+1])
                index += 2
            else:
                index += 1
        return curVal
                
                
                
        
