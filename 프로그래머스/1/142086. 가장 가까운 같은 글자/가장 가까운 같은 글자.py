s = "banana"
def solution(s):
#문자열 s를 리스트로 변환 (인덱스로 접근)
#answer 리스트를 -1로 초기화 (answer의 길이는 곧 s 의 길이)
#현재 문자가 이전에 등장했는지 확인 -> 등장했다면, 그 문자가 마지막으로 나타난 위치를 이용해 거리를 계산 -> . answer 리스트의 해당 인덱스를 업데이트 (-1 에서)
#마지막 answer return
    list_s = list(s)
    k = len(list_s)
    #초기값 설정
    answer = [-1]* k
    appear = {}
   
    for i in range(k):
        alphabet = list_s[i]
        if alphabet in appear:
            #마지막으로 나타난 위치 - : 마지막 
            answer[i] = i - appear[alphabet]
        appear[alphabet] = i #updateeeee (-> 마지막위치가 그럼 바뀜)
    return answer
print(solution(s))