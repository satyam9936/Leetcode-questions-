'''dynamic programming DP 1- optimal solution 
2- overlappping subproblem
3-divide and conquer or greedy algorithm
 DP= Recursion + Memoization
'''
#Top down approach
def fib(n,memo={}):
    if n in memo:
        return memo [n]
    if n<=2:
        return 1
    
    memo[n]=fib(n-1, memo)+fib(n-2, memo)
    return memo[n]

#Bottom up approach
def fib(n):
    if n<=2:
        return 1
    dp=[0]*(n+1) # tabulation
    dp[1]=1
    dp[2]=1

    for i in range (3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]


