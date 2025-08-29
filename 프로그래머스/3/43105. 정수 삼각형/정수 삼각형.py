def solution(triangle):
    N = len(triangle)    
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1,N):
        for j in range(0,i+1):
            if j == 0:
                dp[i][0] = dp[i-1][0] + triangle[i][0]
            elif i == j:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[N-1])
print(solution)

    