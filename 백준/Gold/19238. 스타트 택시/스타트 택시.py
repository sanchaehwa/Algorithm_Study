'''
손님을 도착지로 데려다주면 -> 연료 충전
연료 바닥 나면 -> 업무 종료
M명의 승객
한칸 이동할때마다 -1
도착지로 가면 *2 충전

남은 연료의 양을 구해라 
'''
import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def findStartPosition(start):
    ty,tx = start
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((ty-1,tx-1))
    dist[ty-1][tx-1] = 0
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    while q:
        y,x = q.popleft()
        for i in range(4):
            sy = dy[i] + y
            sx = dx[i] + x
            if 0 <= sy < N and 0 <= sx < N:
                if graph[sy][sx] == 0 and dist[sy][sx] == -1:
                    dist[sy][sx] = dist[y][x] + 1
                    q.append((sy,sx))
    return dist

N,M,E = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
Sy,Sx = map(int,input().split())
#승객의 출발지 행 - 열 / 목적지 행 - 열
client_start = []
client_goal = []
for _ in range(M):
    scy,scx,ecy,ecx = map(int,input().split())
    client_start.append((scy,scx))
    client_goal.append((ecy,ecx))

energy = E
taxi_start = (Sy,Sx)

for _ in range(M):
    dist_from_taxt = findStartPosition(taxi_start)
    candidates = []
    for i in range(len(client_start)):
        sy,sx = client_start[i]
        d = dist_from_taxt[sy-1][sx-1]
        if d != -1: #도달 가능한거
            candidates.append((d,sy,sx,i))
    
    if not candidates:
        print(-1)
        exit()

    candidates.sort()
    dist, sy, sx, idx = candidates[0] #같은 숫자여도 인덱스가 앞에 있는걸 고를수가 있겠지
    
    if energy < dist:
        print(-1)
        exit()

    energy -= dist

    dist_from_client = findStartPosition((sy,sx)) # dist 가 반환이 될거고 
    gy,gx = client_goal[idx]
    goal_dist = dist_from_client[gy-1][gx-1]
    
    if goal_dist == -1 or energy < goal_dist:
        print(-1)
        exit()

    energy -= goal_dist
    energy += goal_dist * 2
    
    taxi_start = (gy,gx)
    client_start.pop(idx) #운행 완료                           
    client_goal.pop(idx) #운행 완료

print(energy)


# def moveTaxi(start,goal,energy):
#     sy,sx = start
#     gy,gx = end
#     visited = [[0] * N for _ in range(N)]
#     q = deque()
#     q.append((sy-1,sx-1,energy))
#     visited[sy][sx] = 1
#     dy = [-1,1,0,0]
#     dx = [0,0,1,-1]
#     while q:
#         y,x,energy = q.popleft()
#         if (y,x) == (gy-1,gx-1):
#             return (y,x,energy * 2)
#         for i in range(4):
#             ty = dy[i] + y
#             tx = dx[i] + x
#             if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx]:
#                 visited[ty][tx] = 1
#                 q.append((sy,sx,energy+1))

