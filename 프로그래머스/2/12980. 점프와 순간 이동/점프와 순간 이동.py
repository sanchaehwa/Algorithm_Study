n =5
def solution(n):


    battery = 0
   
    while n > 0:
        if n % 2 == 0:
            n = n // 2 # 3
        else:
            n -= 1
            battery += 1
        #n -= 이동한거리

    return battery

    


print(solution(n))