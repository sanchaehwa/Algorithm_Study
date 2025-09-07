'''
- 현재 스택에 있는 값 (top) < i => top의 인덱스를 기준으로 
5 /4 5 * (4-idx)
- 스택이 비었다 하면 
(current h , start idx )
'''
import sys
input = sys.stdin.readline


N = int(input())
nums = [int(input().strip()) for _ in range(N)]
stack = []
#넓이 lst
area = []

for idx in range(N):
    start = idx
    while stack and stack[-1][0] > nums[idx]: # 4 - 5 인 경우
        h,pop_idx = stack.pop()
        areas = h * (idx - pop_idx)
        area.append(areas)
        start = pop_idx
    stack.append((nums[idx], start))
while stack: #남은거 계산
    h,pop_idx = stack.pop()
    areas = h * (N-pop_idx)
    area.append(areas)
print(max(area))