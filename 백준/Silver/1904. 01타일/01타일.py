import sys
class Solution:
    def zeroOneTile(self)->int:
        N = int(sys.stdin.readline())
        result = 0
       # dp = [0] * N  : N이 커지면 메모리 초과
        if N == 1: # N이 1이거나 2보다 작으면 Index Error 유발하기에 예외처리
            print(1)
            return
        if N == 2:
            print(2)
            return
        dp = [0] * (N+1) 
        dp[1] = 1
        dp[2] = 2
        for i in range(3,N+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746
        print(dp[N])
solution = Solution()
solution.zeroOneTile()