'''
11
​
10 9
9  8 7
8
.
.
.
.
​
res(11) = min(res(11-1),res(11-2),res(11-5)) 
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = {}
        def helper(amount):
            if amount == 0:
                return 0
            if amount in table:
                return table[amount]
            minMoves = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    minMoves = min(helper(amount-coin)+1,minMoves)
            table[amount] = minMoves
            return minMoves
        res = helper(amount)
