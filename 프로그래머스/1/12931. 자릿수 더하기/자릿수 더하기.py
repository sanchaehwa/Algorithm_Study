#n = 123
def solution(n):
    number = list(map(int,str(n)))
   # print(number)
    answer = sum(i for i in number)
    return answer
#print(solution(n))