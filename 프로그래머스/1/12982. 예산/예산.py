#d = [2,2,3,3,4]	
#budget = 10
def solution(d, budget):
    result = []
    count = 0
    d.sort() #최대 많은 부서에 지원하기 위해서
    for i in d:
      #  print(budget)
        if i <= budget:
            budget -= i
            count += 1
        else:
            break
    return count

#print(solution(d,budget))