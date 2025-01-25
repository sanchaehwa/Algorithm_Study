#a = [1,2,3,4]
#b = [-3,-1,0,2]
def solution(a, b):
    result = []
    for i in range(len(a)):
        angle = a[i] * b[i]
        result.append(angle)
    #print(result)
    answer = sum(result)
    #print(answer)
    return answer
#print(solution(a,b))