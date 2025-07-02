import sys
class Solution:
    def lis1(self)->int:
        N = int(sys.stdin.readline())
        num = list(map(int,sys.stdin.readline().split()))
        dp = [1] * N
        for i in range(0,N):
            for j in range(i):
                if num[j] < num[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        print(max(dp))
solution = Solution()
solution.lis1()
