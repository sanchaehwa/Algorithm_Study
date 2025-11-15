'''
특정 수를 찾아라 ->> 이진 / 이분탐색
정렬된 배열

'''
import sys

input = sys.stdin.readline

def find_x(N,aList,target):
    result = list()
    for t in target:
        st = 0
        en = N-1
        found = False
        while st <= en:
            md = (st+en) // 2
            if t < aList[md]: #en 옮겨
                en  = md -1
            elif t > aList[md]: #st 증가
                st = md + 1
            else:
                found = True
                break
        if found:
            result.append(1)
        else:
            result.append(0)
    return result
    

N  = int(input())

aList = list(map(int,input().split()))
aList.sort(reverse=False)

M = int(input())
target = list(map(int,input().split()))

for i in find_x(N,aList,target):
    print(i)