absolutes = [1, 2, 3]
signs = [False, False, True]

def solution(absolutes, signs):
    result = [] 
    for idx, sign in enumerate(signs):
        number = absolutes[idx]
        if not sign:
            number = -number
        result.append(number)
    answer = sum(result)
   # print(result)
    return answer  
print(solution(absolutes, signs))