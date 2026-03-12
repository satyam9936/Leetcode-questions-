class Solution:
    def count_ways(self, n: int) -> int:
        mod = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, 7):
                if i - j >= 0:
                    dp[i] = (dp[i] + dp[i - j]) % mod

        return dp[n]
    
    #optomized space complexity
    def count_ways(self, n: int) -> int:
        mod = 10**9 + 7
        
        dp = [0] * 6
        dp[0] = 1

        for i in range(1, n + 1):
            new_dp = [0] * 6
            for j in range(1, 7):
                if i - j >= 0:
                    new_dp[j % 6] = (new_dp[j % 6] + dp[(i - j) % 6]) % mod
            dp = new_dp

        return dp[n % 6]