def solve(n, a, b, c):
    dp=[-1e10]*(n+1)
    dp[0]=0
    for i in range(a,n+1):
       dp[i]=max(dp[i],dp[i-a]+1)
    for i in range(b,n+1):
       dp[i]=max(dp[i],dp[i-b]+1)
    for i in range(c,n+1):
       dp[i]=max(dp[i],dp[i-c]+1)
    return dp[n]

       


if __name__ == "__main__":
  n, a, b, c = map(int, input().split())
  print(solve(n, a, b, c))