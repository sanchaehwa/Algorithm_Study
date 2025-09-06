from collections import deque
import math
progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]
def solution(progresses, speeds):
    time_lst = deque()
    for lst in zip(progresses,speeds):
        p,s = lst
        complete_time = 0
        t = 100 - p
        complete_time = math.ceil(t / s)
        time_lst.append(complete_time)
    result = [] #결과를 담을 
    current_max = time_lst[0]
    cnt = 1
    for now in range(1, len(time_lst)):
        if time_lst[now] <= current_max:
            cnt += 1
        else:
            #배포 묶음이 끝나는 경우 * current_max 보다 큰경우 
            result.append(cnt)
            current_max = time_lst[now]
            cnt = 1
    result.append(cnt) # for 문이 끝나고 마지막 묶음을 result에 추가해야함
    return result
solution(progresses, speeds)
