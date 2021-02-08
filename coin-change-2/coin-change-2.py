from collections import Counter
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        table = Counter()
        table[0] = 1
        for coin in coins:
            for x in range(coin,amount+1):
                if (x-coin) not in table:
                    table[x] += 0
                else:
                    table[x] += table[x-coin]
        return table[amount]
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]