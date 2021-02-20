class Solution:
    def intToRoman(self, num: int) -> str:
        IntTable = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        RTable = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        order = ['M','D','C','L','X','V','I']
        res = ""
        for index in range(len(order)):
            c = order[index]
            cVal = RTable[c]
            
            while num >= cVal:
                res += c
                num -= cVal
            
            for smIndex in range(index+1,len(order)):
                smVal = order[smIndex]
                smInt = RTable[smVal]
                
                if cVal - smInt <= num and (cVal-smInt) not in IntTable:
                    num -= (cVal-smInt)
                    res += smVal+c
                    
                    break
            
        return res