class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        demand = 1
        while demand <= n:
            rows += 1
            n -= demand
            demand += 1
        return rows
            
        