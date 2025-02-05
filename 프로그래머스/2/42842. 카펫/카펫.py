brown = 24
yellow = 24
def solution(brown,yellow):
    k = brown + yellow
    rectangle = []
    for i in range(1,k+1):
        if k % i == 0:
            rectangle.append((i, k // i))
    for  x,y in rectangle:
        if (x-2) * (y-2) == yellow: #중앙 배치
            if x >= y: #세로 == 가로 가로> 세로
                return [x,y]
            else: # 세로 > 가로 
                return [y,x]
print(solution(brown,yellow))