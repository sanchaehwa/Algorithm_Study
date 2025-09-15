import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    nums = [int(input().strip()) for _ in range(2)]
    k = nums[0] #y : 층
    n = nums[1] #x : 호

    dp = [[0] * (n+1) for _ in range(k+1)]
    for i in range(1,n+1):
        dp[0][i] = i
    for y in range(1,k+1):
        for x in range(1,n+1):
            dp[y][x] = dp[y][x-1] + dp[y-1][x] 
    print(dp[k][n])
