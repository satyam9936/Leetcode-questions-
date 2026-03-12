def knapsack(values, weight, capacity, items):
    n=len(values)

    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]

    # build dp
    for i in range(1,n+1):
        for w in range (capacity+1):
            if weight[i-1]<=w:
                dp[i][w]=max(dp[i-1][w], dp[i-1][w-weight[i-1]]+values[i-1])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]
