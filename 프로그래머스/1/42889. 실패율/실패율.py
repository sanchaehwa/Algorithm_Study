stages = [2, 1, 2, 6, 2, 4, 3, 3]	
N = 5

def get_counts(stages):
    stages_number = {}
   
    for x in stages:
        if x in stages_number:
            stages_number[x] += 1
        else:
            stages_number[x] = 1
    return stages_number

def solution(N,stages):
    #각 스테이징
    counts = get_counts(stages)
    #stages 길이
    len_stages = len(stages)
    #stages 순회 -> 실패율 저장 배열
    failed = []
    for stage in range(1, N+1):
        if len_stages > 0:
            failed_count = counts.get(stage,0)
            failed_rate = failed_count / len_stages
            failed.append((stage,failed_rate))
            len_stages -= failed_count #다음스테이징
        else:
            failed.append((stage,0))
    #같은 경우 lamda 가 모야
    failed.sort(key=lambda x: (-x[1],x[0]))
    return [stage for stage, _ in failed]
print(solution(N,stages))