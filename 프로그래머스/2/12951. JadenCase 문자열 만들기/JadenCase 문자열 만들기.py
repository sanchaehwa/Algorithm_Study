#s = "3people 3Followed me"
def solution(s):
    s = s.lower()
    list_s = s.split(" ") 
    result = []
    #print(list_s)
    for word in list_s:
        if word:
            if word[0].isdigit():
                result.append(word)
            else:
                result.append(word[0].upper() + word[1:])
        else:
            result.append("")

    return " ".join(result)
        
      
#print(solution(s))
    