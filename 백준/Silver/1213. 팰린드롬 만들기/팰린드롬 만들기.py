        
def solution(name:str)->str:
    count = dict()
    keys = sorted(list(set(name))) #사전순 정렬
    odd = []
    for key in keys:
        cnt = name.count(key)
        count[key] = cnt
        if cnt % 2:
            odd.append(key)
    if len(odd) > 1:
        print("I'm Sorry Hansoo")
        return
    else:
        result = ''
        for key in keys:
            result += key * (count[key] // 2)
        if odd:
            result += odd[0] + result[::-1]
        else:
            result += result[::-1]
    print(result)

name = input()
solution(name)