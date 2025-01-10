#s = "abc"
def solution(s):
    normal_s = s.lower()
#    print(normal_s)
    

    if normal_s.count('p') == normal_s.count('y'):
        return True
    else:
        return False

#print(solution(s))