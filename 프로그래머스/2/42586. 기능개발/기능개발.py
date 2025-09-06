from collections import deque
def solution(progresses, speeds):
    time_lst = deque()
    for lst in zip(progresses,speeds):
        p,s = lst
        complete_time = 0
        t = 100 - p
        complete_time = t // s
        time_lst.append(complete_time)
    result = []
    cnt = 1
    while time_lst:
        while time_lst.pop() >= time_lst[-1]:
            cnt += 1
        result.append(cnt)
    print(result)
    
                