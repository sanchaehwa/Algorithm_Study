from itertools import combinations
#number = [-2,3,0,2,-5]
def solution(number):
    count = 0
    count_len = []
    number_list = list(combinations(number,3))


    for i in number_list:
        #print(sum(i))
       # print(i)
        if sum(i) == 0:
            count_len.append(i)
            count += 1
   # print(number_list)
    #print(count_len)
    return count
#print(solution(number))