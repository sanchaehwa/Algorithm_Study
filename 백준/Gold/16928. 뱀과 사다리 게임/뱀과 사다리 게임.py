'''
1. 주사위 만큼 이동 
2. 이동하다가 뱀이면 뱀 따라서 이동 -> 원래 있던 칸의 번호보다 작아짐
3. 사다리로 이동하면 -> 원래 있던 칸의 번호보다 커짐
start : 1
end : 100

주사위 굴러야하는 횟수 / 최소  => bfs

'''
import sys
from collections import deque
input = sys.stdin.readline


def bfs(target,snake,ladder):
    board = {**ladder, **snake}
    visited = [0] * 101
    q = deque()
    q.append((1,0)) # 시작 위치는 1이고 , 주사위는 0 번 돌렸어
    visited[1] = 1

    while q:
        pos, cnt = q.popleft()
        if pos == target: #100일 경우
            return cnt
        for dice in range(1,7):
            next_pos = pos + dice
            if next_pos > 100:
                continue
            if next_pos in board:
                next_pos = board[next_pos]
            if visited[next_pos] == 0:
                visited[next_pos] = 1
                q.append((next_pos, cnt+1))
    return -1


#사다리수 / 뱀의 수 
N,M = map(int,input().split())

ladder = dict() # 사다리 이동
snake = dict() # 뱀 이동


for _ in range(N):
    y,x = map(int,input().split())
    ladder[y] = x

for _ in range(M):
    u,v = map(int,input().split())
    snake[u] = v

# 1에서 출발
print(bfs(100,snake,ladder))