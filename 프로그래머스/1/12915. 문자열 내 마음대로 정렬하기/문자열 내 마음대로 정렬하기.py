
def solution(strings, n):
    answer = []
    strings.sort()
    answer = sorted(strings, key=lambda word:word[n])
    return answer

