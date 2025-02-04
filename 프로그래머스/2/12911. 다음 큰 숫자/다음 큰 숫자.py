# n - n < x
# n 이진수 1의 개수 == x 이진수 1의 개수
# 이걸 모두 만족하는 가장 작은수가 다음 큰 수
# while - bin (이진수) - if



n = 78
def solution(n):
    #n의 이진수 변환
    bin_n = bin(n)[2:]    
    n_count = str(bin_n).count('1')
    result = []
    x = n + 1
    while n < x :
        #x의 이진수 변환
        x_n = bin(x)[2:]
        #x개수 세기
        x_count = str(x_n).count('1')
        if x_count == n_count:
            break
        x = x+1
    return x

print(solution(n))