#Stack - Pop - append

s = "baabaa"

def solution(s):
    #Stack 초기화
    stack = []
    for element in s: #b a a b a a 
        if stack and stack[-1] == element:
            stack.pop() # aa (pop) bb (pop) aa (pop)
        else:
            stack.append(element) # b -> a -> a
    #성공적으로 수행할수 있는지 아닌지 (-> 빈리스트이면 성공 / 빈 리스트가 아니면 실패)
    if len(stack) == 0:
        return 1
    else:
        return 0
    