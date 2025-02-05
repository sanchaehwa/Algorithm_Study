n = 5
def solution(n):
    a = 1 #F(1)
    b = 1 #F(2)
    #F(1) / F(2)
    if n == 1 or n ==2:
        return 1 % 1234567
    #F(3) - 
    for _ in range(1,n):
        a,b = b, a+b
    return a % 1234567
    
print(solution(n))