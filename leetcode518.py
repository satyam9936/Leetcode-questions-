#coin changes 
from ast import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] will store the number of combinations to make up amount i
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: there's one way to make amount 0 (using no coins)

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]