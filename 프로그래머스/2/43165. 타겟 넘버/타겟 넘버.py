# numbers = [1,1,1,1,1]
# target = 3
# def solution(numbers, target):
#     cnt = 0
#     q = deque()
#     q.append((0,0))

#     while q:
#         idx,t = q.popleft()
#         if idx == len(numbers):
#             if t == target:
#                 cnt += 1
#         if idx < len(numbers):
#             q.append((idx+1, t + numbers[idx]))
#             q.append((idx+1, t - numbers[idx]))
#     return cnt

# print(solution(numbers,target)

# def solution(numbers, target):
#     answer = dfs(numbers,target,0) #depth가 0
#     return answer

# def dfs(numbers, target, depth):
#     answer = 0
#     #모든 경우의수를 탐색한다
#     if depth == len(numbers): #트리의 끝에 도달한 경우
#         #print(numbers)
#         return 1 if sum(numbers) == target else 0
#     else:
#         answer += dfs(numbers,target,depth+1) #+n
#         numbers[depth] *= -1 # -n
#         answer += dfs(numbers, target, depth+1) #-n
#         return answer

def dfs(numbers, target, depth, total):
    if depth == len(numbers):
        return 1 if total == target else 0
    count = dfs(numbers, target, depth+1, total+numbers[depth])
    count += dfs(numbers, target, depth+1, total - numbers[depth])
    return count
def solution(numbers, target):
    answer = dfs(numbers, target,0,0)
    return answer