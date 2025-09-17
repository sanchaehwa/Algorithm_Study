import sys
input = sys.stdin.readline


coins = [500,100,50,10,5,1] #무한대
pay = int(input())
K = 1000 - pay #620
result = 0 #동전의 개수

for i in coins:
    result += K // i
    if K == 0:
        break
    K = K % i
print(result)