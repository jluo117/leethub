class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        stk = []
        tolCost = 0
        for c,cost in zip(s,cost):
            if len(stk) and stk[-1][0] == c:
                if stk[-1][1] > cost:
                    tolCost += cost
                    continue
                else:
                    tolCost += stk[-1][1]
                    stk.pop()
            stk.append((c,cost))
        return tolCost
                    
                
        