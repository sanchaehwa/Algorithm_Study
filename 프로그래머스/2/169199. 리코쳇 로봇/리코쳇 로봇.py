from collections import deque

def solution(board):
    # board를 2차원 리스트로 변환
    graph = [list(row) for row in board]
    B = len(graph)
    A = len(graph[0])
    
    # R, G 위치 찾기
    for i in range(B):
        for j in range(A):
            if graph[i][j] == 'R':
                start = (i, j)
            elif graph[i][j] == 'G':
                end = (i, j)
    
    # BFS
    def bfs(start, end):
        sy, sx = start
        ey, ex = end
        visited = [[-1] * A for _ in range(B)]
        visited[sy][sx] = 0
        q = deque()
        q.append((sy, sx))
        dy = [-1, 1, 0, 0]
        dx = [0, 0, 1, -1]
        
        while q:
            y, x = q.popleft()
            if (y, x) == (ey, ex):
                return visited[y][x]
            
            for i in range(4):
                ny, nx = y, x
                # 끝까지 이동
                while True:
                    ty = ny + dy[i]
                    tx = nx + dx[i]
                    if 0 <= ty < B and 0 <= tx < A and graph[ty][tx] != 'D':
                        ny, nx = ty, tx
                    else:
                        break
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
        return -1
    
    return bfs(start, end)