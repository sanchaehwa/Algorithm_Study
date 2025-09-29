import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int,input().split())))
M = int(input())
F = list(map(int,input().split()))

for f in F:
    st = 0
    en = N-1
    md = (st+en) // 2
    flag = False
    while st <= en:
        md = (st+en) // 2
        if A[md] == f:
            print(1)
            flag = True
            break
        elif A[md] < f:
            st = md +1
        else:
            en = md -1
    if not flag:
        print(0)

    