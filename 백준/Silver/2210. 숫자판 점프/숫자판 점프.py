import sys

#5 * 5 숫자판
graph = [list(map(int,sys.stdin.readline().split()))for _ in range(5)]
result = set()

def dfs(x,y,num,depth):

    if depth== 6:
        result.add(num)
        return
    #상하좌우
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    
    for i in range(4):
        nx, ny = dx[i] + x , dy[i] + y
        #탐색 수 
        if 0 <= nx < 5 and 0 <= ny < 5:
            #문자열로 이어 붙이기
            dfs(nx,ny,num + str(graph[nx][ny]),depth+1)

#visited = True, False 대신에 이미 존재하는 수면 append 안하는 식으로 하면 안되나..?
#시작점 
for i in range(5):
    for j in range(5):
        dfs(i,j,str(graph[i][j]),1)
print(len(result))