import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for _ in range(N+1)]

for i in range(10):
    dp[1][i] = 1

for n in range(2,N+1):
    for i in range(10):
        if i == 0:
            dp[n][i] = 1
        else:
            dp[n][i] = dp[n-1][i] + dp[n][i-1]
print(sum(dp[N])% 10007)