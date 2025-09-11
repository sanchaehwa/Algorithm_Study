'''
- 앞번호의 학생 / 뒷번호의 학생에게만 체육복을 빌려줄수 있다 (3 - 2,4)
- 체육복을 빌려서 최대한 많이 체육수업을 들을 수 있도록
- 여벌 체육복을 가져온 학생도 체육복을 도난 당할 수 있다 lost 에 있는게 reserve에도 있다는거고 도난당하면 하나이기때문에 빌려줄수가 없음 => reserve에서 제외 시켜야하는거
'''


def solution(n, lost, reserve):
    # 일단 체육을 들을 수 있는 학생 * 확정 case (전체 - 잃어버린 = 들을수있는 학생)
    answer = n - len(lost)
    #앞번호 학생 . 뒷번호 학생 이면 앞번호부터 제거해나가야되지
    lost = sorted(lost, reverse=True)
    for i in range(1,n+1): # 1 ~ 6
        if i in lost and i in reserve:
            answer += 1
            lost.remove(i)
            reserve.remove(i)
    #도난 당한 친구가 없을때까지 반복해서 최대한 많은 학생이 들을 수있도록
    while len(lost) > 0:
        l = lost.pop() #도난당한 학생
        if l-1 in reserve: #앞번호 학생이 여벌인 경우
            reserve.remove(l-1)
            answer += 1
        elif l+1 in reserve:
            reserve.remove(l+1)
            answer += 1
    return answer
            