#keymap = ["ABACD", "BCEFD"]	
#targets = ["ABCD","AABB"]	

def solution(keymap, targets):
    answer = []
    for i in targets:
        total = 0  
        insert = True  
        for j in i:  
            find = False  
            case = float('inf') 

            for k in keymap: 
                if j in k:
                    find = True
                    case = min(case, k.index(j) + 1) 

            if find:
                total += case  
            else:
                insert = False  
                answer.append(-1)
                break 
        if insert: 
            answer.append(total)

    return answer
#print(solution(keymap,targets))