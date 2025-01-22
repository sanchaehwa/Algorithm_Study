#arr = [1,2,3,4]
def solution(arr):
    sum = 0
    for i in arr:
        sum += i
    answer = sum / len(arr)
    return answer
#print(solution(arr))