import sys
input = sys.stdin.readline

# 1. 철수 빙고판 (5x5)
ipt = [list(map(int, input().split())) for _ in range(10)]
board = ipt[:5]  # 0~4행: 빙고판
calls = sum(ipt[5:], [])  # 5~9행: 사회자가 부르는 숫자들 (25개) → 1차원으로 펴기

# 2. 빙고 줄 개수 세기 함수
def count_bingo(b):
    bingo = 0
    # 가로
    for row in b:
        if row.count(0) == 5:
            bingo += 1
    # 세로
    for col in zip(*b):
        if list(col).count(0) == 5:
            bingo += 1
    # 대각선 2개
    if all(b[i][i] == 0 for i in range(5)):
        bingo += 1
    if all(b[i][4-i] == 0 for i in range(5)):
        bingo += 1
    return bingo

# 3. 숫자 하나씩 부르면서 체크
for i in range(25):
    called = calls[i]
    # 숫자 위치 찾아서 0으로 표시
    for y in range(5):
        for x in range(5):
            if board[y][x] == called:
                board[y][x] = 0
                break
    # 빙고 줄 3개 이상이면 출력하고 종료
    if count_bingo(board) >= 3:
        print(i + 1)  # i는 0부터 시작하므로 +1
        break