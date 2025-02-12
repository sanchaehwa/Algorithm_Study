#n = 8 #벽 길이
#m = 4 #걸레 길이
#section = [2,3,6] #다시 칠해야 하는 경우

def solution(n,m,section):
    # index = 0
    # count = 0
    # picture = [i for i in range(1,n+1)]
    # start = section[index]
    # print(picture[index:index+m])
    # for _ in picture:
    #     if picture[index] == start:
    #             if picture[index:index+m] == section:
    #                     count += 1
    #                     del picture[index:index+m]
    #     count += 1
    #     del picture[index]
    #     index += 1
    # print(count)
    index = 0
    count = 0
    while index < len(section):
        #시작지점
        start = section[index]
        #페인트 칠하는 횟수
        count += 1
        #룰러가 덮을수있는지점 start+m 룰러가 덮을 있는 범위 안에서 index 증가 
        while index < len(section) and section[index] < start + m:
            index +=1
    return count
#print(solution(n,m,section))