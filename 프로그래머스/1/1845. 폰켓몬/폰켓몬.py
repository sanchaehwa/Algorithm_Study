#가져온값이 key값이 같으면 다시 하나 들고 오거나 그런식으로?
from collections import Counter #리스트에서 딕셔너리로 바꾸기 위해 쓰는 함수
nums = [3,3,3,2,2,2]
def solution(nums):
    N = int(len(nums)/2)
    pocket = dict(Counter(nums))    
    answer = min(len(pocket),N)
    return answer
print(solution(nums))