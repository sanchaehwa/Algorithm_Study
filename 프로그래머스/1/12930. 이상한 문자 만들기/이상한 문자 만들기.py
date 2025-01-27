#공백기준 문자열 슬라이싱 하기
s = "try hello word"
def solution(s):
    list_s = s.split(' ')
    print(list_s)
    result = []
    for i in list_s:
        answer = ''
        for j in range(len(i)):
            
            if j == 0:
                answer += i[j].upper()
            elif j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        result.append(answer)
    return ' '.join(result)

    #print(list_s)       
   # return answer
print(solution(s))