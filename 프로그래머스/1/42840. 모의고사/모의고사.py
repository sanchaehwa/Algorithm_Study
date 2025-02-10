answers = [1,2,3,4,5]	

def split(lst,answers):
    count = 0
   # lst_split = [lst[i:i+size] for i in range(0,len(lst),size)]
    for i in range(len(answers)):
       # print(lst_split)
        if answers[i] == lst[i % len(lst)]:
            count += 1
    return count


def solution(answers):
    person1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    #size = len(answers)
    answer = []

   # person1_score = split(person1,answers)
    #person2_score = split(person2,answers)
   # person3_score = split(person3,answers)
  #  scores = [person1_score,person2_score,person3_score]
    scores = [split(person1,answers),split(person2,answers),split(person3,answers)]
    #print(scores)
    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx+1)
    return answer
print(solution(answers))
