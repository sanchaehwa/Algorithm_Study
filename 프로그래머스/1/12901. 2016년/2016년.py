#a = 5
#b = 24
def solution(a, b):
   
    calendar = [5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    calendar_number = calendar[a-1]
   # print(calendar_number)
   #윤년이라 -1
    find_day = int((b-1) + calendar_number) % 7
    #print(find_day)
    answer = day[find_day]

    return answer
#print(solution(a,b))