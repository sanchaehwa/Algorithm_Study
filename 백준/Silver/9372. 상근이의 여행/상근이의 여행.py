import sys
from collections import deque
input = sys.stdin.readline


#테스트 케이스 개수
T = int(input())

for _ in range(T):
    #국가의 수 / 비행기 종류
    N,M = map(int,input().split())
    #양방향 배열
    for _ in range(M):
        input()
    print(N-1)