
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    i = 0
    for word in A:
        answer += (word * B[i])
        i += 1
    return answer
