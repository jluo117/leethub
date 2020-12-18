'''
76,75,74,73
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk = []
        res = [0] * len(T)
        for index in range(len(T)-1,-1,-1):
            while len(stk) > 0 and stk[-1][0] <= T[index]:
                stk.pop()
            if len(stk) == 0:
                res[index] = 0
            else:
                res[index] = stk[-1][1] - index
            stk.append((T[index],index))
        return res
        
