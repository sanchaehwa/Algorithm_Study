#price = 3
#money = 30
#count = 4
def solution(price, money, count):
    increase_money = 0
    #print(increase)
    for i in range(1,count+1):
        increase_money+=(price*i)
    answer = increase_money - money
    return max(0, answer) #금액이 부족하지않는 경우 0 을 return 
#print(solution(price,money,count))