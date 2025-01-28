#s = "a B z "
n = 4
def solution(s, n):
    answer = ''
    alphabet_upper = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    alphabet_lower = [chr(i) for i in range(ord('a'),ord('z')+1)]
    s_split = list(s)
   # print(s_split)
    for idx,i in enumerate(s_split):
        if 'A' <= i <= 'Z':
            alphabet_index = alphabet_upper.index(i)
            i = alphabet_upper[(alphabet_index + n) % 26]
          #  print(i)
        elif 'a' <= i <= 'z':
            alphabet_index = alphabet_lower.index(i)
            i = alphabet_lower[(alphabet_index + n) % 26]
           # print(i)
        answer += i
    return answer
#print(solution(s,n))