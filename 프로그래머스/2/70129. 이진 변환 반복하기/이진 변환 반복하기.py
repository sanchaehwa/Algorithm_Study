#s ="110010101001"
#result = [3,8]
def solution(s):
    count = 0 #이진 변환 횟수
    del_zero = 0 #지워진 0의 갯수
    while s != "1":
        # 110010101001
        del_zero += s.count("0")
        s = s.replace("0","")
        # 111111
        len_s = len(s) # 6
        s = bin(len_s)[2:] #이진수 110
        count += 1
    return [count,del_zero]

#print(solution(s))