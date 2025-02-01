cards1 =["i", "drink", "water"]	
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
result = "Yes"
def solution(cards1, cards2, goal):
    i = 0
    j = 0
    for word in goal:
        if i < len(cards1) and word == cards1[i]: 
            i += 1
        elif j < len(cards2) and word == cards2[j]: 
            j += 1
        else: return "No"
    return "Yes"
    
#print(solution(cards1,cards2,goal))