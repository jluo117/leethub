class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk = []
        res = [0] * len(T)
        for index in range(len(T)-1,-1,-1):
            while stk and stk[-1][0] <= T[index]:
                stk.pop()
            if len(stk):
                res[index] = stk[-1][1] - index
            stk.append((T[index],index))
        return res