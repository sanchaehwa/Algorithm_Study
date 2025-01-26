#기사단원 명수 number / 제한 3 / power 2 /
#기사단원 명수의 약수 개수 구하고 그걸 하나의 리스트에 저장한뒤에 순회하면서 제한보다 큰지확인하고 크면 2를 넣어
# 그 리스트 다 더하면 answer
#number = 10
#limit = 3
#power = 2

def solution(number, limit, power):
    #기사단원
    demon_slayers = [i +1 for i in range(number)]
    blade = []
    #result = []
    #약수
    for i in demon_slayers:
        count = 0
        sqrt_i = int(i ** 0.5)
        for j in range(1,sqrt_i+1):
            if i % j == 0:
                count += 2 if j * j != i else 1
        blade.append(count)
    answer = sum(power if x > limit else x for x in blade)
   
    #print(result)
    #print(answer)
    return answer
    

#print(solution(number,limit,power))