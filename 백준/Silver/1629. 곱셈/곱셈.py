import sys

input = sys.stdin.readline

'''
1. 나눠서 계산하고 그 수만큼 C로 나뉘어도 그 나머지는 내가 다 곱해서 나눈 나머지랑 같다 => 모듈러 연산의 특징
2. 짝수이면 2만큼 나누고 나머지를 구하고 
3. 홀수이면 2만큼 나눈것에 2를 곱하고 거기에 다시 A를 곱해
'''
def reduce_pow(a, b, c):
    if (b == 1):
        return a % c

    X = reduce_pow(a, b//2, c)

    if (b % 2 == 0): # 짝수라면
        return X * X % c
    else: # 홀수라면
        return a * X * X % c

A, B, C = map(int, input().split())

print(reduce_pow(A, B, C))