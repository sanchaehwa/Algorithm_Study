def solution(board, k):
    lst = []
    y = len(board)
    x = len(board[0])
    print(y,x)
    for i in range(y):
        for j in range(x):
            if i + j <= k:
                lst.append(board[i][j])
    return sum(lst)

