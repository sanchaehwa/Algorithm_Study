import sys
input = sys.stdin.readline

# 상, 하, 좌, 우 (문제 기준 1~4에 맞게 정의)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# ← ↓ → ↑ (나선 순서)
spiral_dy = [0, 1, 0, -1]
spiral_dx = [-1, 0, 1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magic = [list(map(int, input().split())) for _ in range(M)]
shark = (N//2, N//2)

bomb_count = [0, 0, 0, 0]

def get_spiral_order():
    order = []
    y, x = shark
    length = 1
    d = 0
    while True:
        for _ in range(2):
            for _ in range(length):
                y += spiral_dy[d]
                x += spiral_dx[d]
                if not (0 <= y < N and 0 <= x < N):
                    return order
                order.append((y, x))
            d = (d + 1) % 4
        length += 1

spiral_order = get_spiral_order()

def flatten_board():
    return [board[y][x] for y, x in spiral_order if board[y][x] != 0]

def update_board(spiral):
    for idx, (y, x) in enumerate(spiral_order):
        if idx < len(spiral):
            board[y][x] = spiral[idx]
        else:
            board[y][x] = 0

def cast_magic(d, s):
    d -= 1
    for dist in range(1, s+1):
        ny = shark[0] + dy[d] * dist
        nx = shark[1] + dx[d] * dist
        if 0 <= ny < N and 0 <= nx < N:
            board[ny][nx] = 0

def explode(spiral):
    global bomb_count
    new_spiral = []
    i = 0
    exploded = False
    while i < len(spiral):
        j = i
        while j < len(spiral) and spiral[i] == spiral[j]:
            j += 1
        if j - i >= 4:
            bomb_count[spiral[i]] += (j - i)
            exploded = True
        else:
            new_spiral.extend(spiral[i:j])
        i = j
    return new_spiral, exploded

def group_convert(spiral):
    new_spiral = []
    i = 0
    while i < len(spiral):
        j = i
        while j < len(spiral) and spiral[i] == spiral[j]:
            j += 1
        new_spiral.extend([j - i, spiral[i]])
        i = j
    return new_spiral[:N*N-1]

# 메인 로직
for d, s in magic:
    cast_magic(d, s)
    spiral = flatten_board()
    
    while True:
        spiral, exploded = explode(spiral)
        if not exploded:
            break
    
    spiral = group_convert(spiral)
    update_board(spiral)

# 결과 출력
print(bomb_count[1]*1 + bomb_count[2]*2 + bomb_count[3]*3)