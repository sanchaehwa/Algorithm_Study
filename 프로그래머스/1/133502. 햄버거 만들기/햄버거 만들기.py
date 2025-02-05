# 1. 배열을 탐색하면서 n번째 인덱스가 1인지 확인
# 2. 만약 arr[n] == 1 이라면:
#    arr[n:n+4](즉, n부터 n+3까지의 부분 배열)이[1,2,3,1]과 같은지 확인
#      같다면:count 증가 (햄버거 포장 횟수)
#       해당 부분 배열을 리스트에서 제거하고 리스트를 다시 처음부터 탐색 
#ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

def solution(ingredient):
    hambuger = [1,2,3,1]
    count = 0
    i = 0
   # print(len(ingredient))
    #4개가 빠졌을떄의 원소의 길이 고려
    while i <= len(ingredient) -len(hambuger): 
        if ingredient[i] == 1:
            if ingredient[i:i+4] == hambuger:
                count += 1
                del ingredient[i:i+4]
                #1이면 음수이면 0 부터 시작하게하래 ...
                i = max (0,i-3)
                continue
        i += 1

    return count
#print(solution(ingredient))