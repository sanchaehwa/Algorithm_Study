def solution(s):
    stack = []
    lst = []
    for i in s:
        if stack and stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return False
    return True