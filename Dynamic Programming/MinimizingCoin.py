#minimizing coin changes 

class Solution:
    def coin_change(self, coins: list[int], amount: int) -> int:
        # dp[i] will store the minimum number of coins needed to make up amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: no coins needed to make amount 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[x] -1 if dp[x] != float('inf') else -1