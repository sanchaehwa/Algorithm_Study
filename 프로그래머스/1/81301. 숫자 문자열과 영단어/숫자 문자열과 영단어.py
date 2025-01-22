#s = "one4seveneight"

def solution(s):
    word_map = {
    "zero": "0", "one": "1", "two": "2", "three": "3", 
    "four": "4", "five": "5", "six": "6", "seven": "7", 
    "eight": "8", "nine": "9"
}
    result = s
    for word,number in word_map.items():
        result = result.replace(word,number)
    return int(result)
#print(solution(s))