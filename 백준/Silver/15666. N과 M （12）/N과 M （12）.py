import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(set(map(int, input().split())))
n = len(lst)
seq = []

def recur(start, depth):
    if depth == M:
        print(' '.join(map(str, seq)))
        return
    for i in range(start, n):
        seq.append(lst[i])
        recur(i, depth+1)  
        seq.pop()

recur(0, 0)