#n = 6


def solution(n):
    count = 0
    while n != 1 and count <= 500:
            if n % 2 == 0:
                n = n // 2

            else:
                n = (n * 3) + 1 
                
            count += 1
    if n == 1:
         return count
    else:
         return -1
#print(solution(n))