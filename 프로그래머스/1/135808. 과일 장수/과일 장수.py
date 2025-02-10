# 리스트 append 가장 큰거 다음으로 큰거 이렇게  -> 내림차순 정렬

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	
def solution(k,m,score):
    score.sort(reverse=True)
    score_list = []
    answer = 0
    index = 0
    while len(score) >= index + m:
        score_list.append(score[index : index + m])
        index += m
  
    for i in score_list:
        answer +=  m * min(i)
       # print(result)

    return answer
#print(solution(k,m,score))