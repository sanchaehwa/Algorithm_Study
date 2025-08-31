import sys
input = sys.stdin.readline

T = int(input())
# N은 40보다 작거나 같은 자연수 또는 0이다
dp_0 = [0] * 41
dp_1 = [0] * 41

dp_0[0],dp_1[0] = 1,0
dp_0[1],dp_1[1] = 0,1

for i in range(2,41): #dp[4] = dp[0] + dp[1] + dp[1] + dp[0] * 0 과 1로 이루어져 있음
    dp_0[i] = dp_0[i-1] + dp_0[i-2]
    dp_1[i] = dp_1[i-1] + dp_1[i-2]

for _ in range(T):
    N = int(input())
    print(dp_0[N],dp_1[N])