#t="3141592"
#p="271" 
def list_change(number):
    result = []
    for i in number:
        result.append(int(i))
    return result

def pointer(t, p):
    t_list = list_change(t)
    t_len = len(t_list)
    p_len = len(p)
    
    pointer_list = []

    start = 0
    end = start + p_len - 1

    while end < t_len:
        number = int("".join(map(str, t_list[start:end + 1])))
        #t로 만들수 있는 부분수열
        pointer_list.append(number)

        # 포인터 이동
        start += 1
        end += 1

    return pointer_list

def solution(t, p):
    
    list_pointer = pointer(t, p)
    values = []
    #문자열 -> 정수
    int_p = int(p)    
    for i in list_pointer:
            #271보다 작거나 같은가
        if i <= int_p:
            values.append(i)
           # print(values)
                #그런 경우의 갯수
            answer = len(values)
    return answer
#print(solution(t,p))