import sys
input = sys.stdin.readline

#랜선의 개수 / 필요한 랜선의 개수

def find_N(N,length):
    st = 1
    en = max(length)
    answer = 0
    while st <= en:
        md = (st + en) // 2
        cnt = 0
        for l in length:
            cnt += l // md
        if cnt < N:
            en = md -1
        elif cnt >= N:
            st = md + 1
            answer = max(answer,md)
    return answer
K,N = map(int,input().split())
lengths = [int(input().strip()) for _ in range(K)]
print(find_N(N,lengths))