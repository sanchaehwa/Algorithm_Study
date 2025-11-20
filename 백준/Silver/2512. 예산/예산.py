import sys
input = sys.stdin.readline

def max_budget(N,budget, M) -> int:
    if sum(budget) <= M:
        return max(budget)
    else:
        st = 0
        en = max(budget)
        cap = 0
        while st <= en:
            md =(st + en) //2
            case1 = 0
            for i in budget:
                if i <= md:
                    case1 += i
                else:
                    case1 += md
            if case1 <= M:
                cap = md
                st = md + 1
            else: #상환액 보다 큰경우이니깐
                en = md - 1
    return cap
                
        

#지방의 수
N = int(input())
#예산
budget  = list(map(int,input().split()))
#총 예산
M = int(input())

print(max_budget(N,budget,M))