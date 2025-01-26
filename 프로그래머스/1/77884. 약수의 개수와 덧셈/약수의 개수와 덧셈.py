#left = 13
#right = 17
def solution(left, right):
    list_number = [i for i in range(left,right+1)]
    #print(list_number)
    answer  = 0
    for i in list_number:
        count = 0
        sqrt_i = int(i**0.5)
        for j in range(1,sqrt_i+1):
            if i % j == 0:
                count += 2 if j * j != i else 1
        if count % 2 == 0:
                answer += i
        else:
                answer -= i

    return answer
  
#print(solution(left,right))