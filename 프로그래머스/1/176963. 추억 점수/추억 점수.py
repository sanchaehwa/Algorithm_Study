def solution(name,yearning,photo):
    answer = []
    info = dict(zip(name,yearning))
    for x in photo:
        count = 0
        for j in x:
            count += info.get(j,0)
        answer.append(count)
    return answer

    