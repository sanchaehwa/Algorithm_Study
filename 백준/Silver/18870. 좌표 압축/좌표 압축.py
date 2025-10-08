import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
lst = nums.copy()
sorted_nums = sorted(set(lst))

def find_st(t,sorted_nums):
    st,en = 0, len(sorted_nums)-1
    md = (st+en) // 2
    while st <= en:
        md = (st+en) // 2
        if sorted_nums[md] < t:
            st = md + 1
        else:
            en = md - 1
    return st
result = []
for i in nums:
    result.append(find_st(i,sorted_nums))
print(' '.join(map(str,result)))