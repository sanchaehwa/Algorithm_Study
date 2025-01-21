#t="3141592"
#
def solution(t,p):
    list_t = [int(char) for char in t]
    list_p = [int(char) for char in p]
    #t_len
    k = len(list_t)
    #p_len
    j = len(list_p)
   
    pointer_list = []
    start = 0
    end = start + j -1
    #부분문자열
    while end < k:
        number = int("".join(map(str,list_t[start:end + 1])))
        pointer_list.append(number)
        start += 1
        end += 1
        
    #print(pointer_list)
    #부분문자열 중에서도 조건에 맞는걸 answer로

    values = []
    int_p = int(p)
    for i in pointer_list:
        if i <= int_p:
            values.append(i)
            answer = len(values)
            #print(answer)
    return answer
#print(solution(t,p))
