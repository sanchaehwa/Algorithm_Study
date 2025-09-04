import sys
input = sys.stdin.readline


#음의수 / 프렛의 수 P
N,P = map(int,input().split())
stack = []
move = 0
lst = dict()
for _ in range(N):
    A,B = map(int,input().split())
    if A not in lst:
        lst[A] = []
    lst[A].append(B)
result = 0
for _, values in lst.items():
    stack = []
    move = 0
    for v in values:
        while stack and stack[-1] > v:
            stack.pop()
            move += 1
        if not stack or stack[-1] != v:
            stack.append(v)
            move += 1
    result += move
print(result)