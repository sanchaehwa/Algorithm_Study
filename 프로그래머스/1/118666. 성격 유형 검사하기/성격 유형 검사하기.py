#survey = ["AN", "CF", "MJ", "RT", "NA"]	
#choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    score_dict = {}
    score_map = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3} 
    character_map = {1 : ['R','T'], 2 : ['C','F'],3 : ['J','M'],4 : ['A','N']}
    for i in range(len(survey)):
        first,second = survey[i]
        choice = choices[i]
        if choice < 4:
            score_dict[first] = score_dict.get(first,0) + score_map[choice]
        elif choice > 4:
            score_dict[second] = score_dict.get(second,0) +score_map[choice]
   # print(score_dict)
    answer = ''
    
    for j in character_map.values():
        character_1, character_2 = j
        score1 = score_dict.get(character_1,0)
        score2 = score_dict.get(character_2,0)
        if score1 > score2:
            answer +=character_1
        elif score1 < score2:
            answer +=character_2
        else: #score1 == score2 
            answer += min(character_1,character_2)
    return answer
#print(solution(survey,choices))