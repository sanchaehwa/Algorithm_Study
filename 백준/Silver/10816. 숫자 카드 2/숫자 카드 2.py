import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
nums.sort()
# 상근이가 가지고 있는 카드
M = int(input())
cards = list(map(int,input().split()))

def first_find(c):
    st,en = 0,N-1
    md = (st+en) // 2
    while st <= en:
        md = (st+en) //2
        if nums[md] < c:
            st = md +1
        else:
            en = md - 1
    return st
def second_find(nums,c):
    st,en = 0,N-1
    while st <= en:
        md = (st+en) // 2
        if nums[md] <= c:
            st = md + 1
        else:
            en = md - 1
    return st
lst = []
for c in cards:
    lst.append(abs(first_find(c) - second_find(nums,c)))
print(" ".join(map(str,lst)))