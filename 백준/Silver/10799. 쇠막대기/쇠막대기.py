import sys
input = sys.stdin.readline
s = input().strip()
stack = []
result = 0
for i in range(len(s)):

    if stack and s[i] == ')':
        #현재 스택의 ( 의 인덱스
        #레이저인 경우
        if i - stack[-1] == 1: #레이저인 경우
            stack.pop()
            result += len(stack)
        #스틱인 경우
        else:
            result += 1
            stack.pop()
    #스택이 비어있거나 ) 를 만나지 못한경우 -> 인덱스
    if s[i] == '(':
        stack.append(i)
'''
( =>위치 A
) =>위치 B

if A - B == 1: #바로 다음에 오는 경우
    raiser #레이저 생성
elif B - A > 1: #막대가 생성된 경우
    stick + 1 #스틱 개수를 B-A만큼 해주던가 아니면 stack 길이만큼이 곧 스틱 개수이다고 봐야하거나

'''
print(result)