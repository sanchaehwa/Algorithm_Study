#array = [1, 5, 2, 6, 3, 7, 4]	
#commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
def solution(array, commands):
    #number = []
    answer = []
    j = len(commands)
   # print(j)
    for i in range(j):
        start,end,k = commands[i]
        p = array[start-1:end]
        p.sort(reverse=False)
        answer.append(p[k-1])
    return answer
#print(solution(array,commands))
        
