
def solution(a, b):
    number = list(range(a,b+1))
   # print(number)
    answer = 0
    for i in number:
        answer += i
    if a > b:
        number = list(range(b,a+1))  
        answer = 0
        for i in number:
            answer += i  
    return answer
