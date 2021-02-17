'''

'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]* len(T)
        stk = []
        for index in range(len(T)-1,-1,-1):
            while len(stk) and stk[-1][0] <= T[index]:
                stk.pop()
            if len(stk):
                res[index] = stk[-1][1] - index
            stk.append((T[index],index))
        return res
        
        