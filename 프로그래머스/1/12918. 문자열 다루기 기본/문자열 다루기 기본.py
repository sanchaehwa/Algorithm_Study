#s = "12344"
def solution(s):
    k = len(s)
    # 조건 1이 4 이거 6 이면 일단 True
    if k == 4 or k ==6:
        #문자열에 문자가 포함되어있는 경우에 False를 Return 하는 내장함수 사용 
        return(s.isdigit())
    
    return False
#print(solution(s))