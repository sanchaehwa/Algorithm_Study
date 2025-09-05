import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

cnt = 0
stack = []
couple = 0
for n in nums:
    count = 1
    while stack and stack[-1][0] < n:
        couple += stack[-1][1]
        stack.pop()
    if stack and stack[-1][0] == n: #나랑 같아 그러면
        same_h, same_count = stack.pop()
        couple += same_count
        count += same_count
        if stack:
            couple += 1
    else: # h > n
        if stack:
            couple += 1
    stack.append((n,count))
print(couple)