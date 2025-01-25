s = "qwer"
def solution(s):
    answer = []
    list_s = list(s)
    len_s = len(list_s) 
   #print(len_s)
    k = int(len_s/2)
    #print(k)
    #answer = str(list_s[k])
    #print(list_s[k:k+2])
    if len_s % 2 == 0:
        answer.extend(list_s[k-1:k+1])
    else:
        answer.extend(list_s[k])
    #print(answer)
    return str("".join(answer))
print(solution(s))