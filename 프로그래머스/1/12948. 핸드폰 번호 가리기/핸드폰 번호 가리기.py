#phone_number="01033334444"
def solution(phone_number):
    
    phone_number_list = list(phone_number)
    k = len(phone_number_list)-4
    #뒤에서 4번째
    last_number = phone_number_list[k:]
    answer = ["*" for i in range(k)]
    answer.extend(last_number)
    result = "".join(answer)
   # print(result)
    return result
    

#print(solution(phone_number))