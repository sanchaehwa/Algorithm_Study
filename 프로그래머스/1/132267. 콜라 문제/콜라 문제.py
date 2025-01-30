#a = 3
#b = 1
#n = 20

def solution(a,b,n):
    coke = 0
    while n >= a:
        #몫
        coke_exchange = (n // a) * b
        no_exchange = n % a
        coke += coke_exchange
        n = coke_exchange + no_exchange
    return coke

#print(solution(a,b,n))