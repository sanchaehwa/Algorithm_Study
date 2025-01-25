# 명예의 전당 저장할 리스트 : 길이는 k 
# k일까지는 무조건 추가하고 
# 해당 리스트의 최소랑 비교했을때 k 이후부터는 score이 더 크면 해당 리스트의 최소를 빼주고 score를 넣어주면 되지..

#score = [10,100,20,150,1,100,200]
#k = 3
def solution(k,score):
    answer = []
    temple = []
    for i in score:
        temple.extend([i])
        temple.sort(reverse=True)
        if len(temple) > k:
            temple.pop()
        answer.append(temple[-1])   
        
    #print(answer)
    return answer
#print(solution(k,score))
