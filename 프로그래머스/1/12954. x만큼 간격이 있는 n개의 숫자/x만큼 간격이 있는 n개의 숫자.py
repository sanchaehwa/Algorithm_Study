#x = 2
#n = 5
def solution(x, n):
    #컴프리헨션 : 표현식 for 변수 in 반복
    answer = [i*x for i in range(1,n+1)]
    return answer
#print(solution(x,n))