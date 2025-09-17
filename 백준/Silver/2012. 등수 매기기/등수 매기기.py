import sys
input = sys.stdin.readline



N = int(input())

student = [int(input().strip()) for _ in range(N)]
student.sort()

result = 0
for idx,r in enumerate(student,start=1): #1부터 시작한다는거 0이 아니라
    result += abs(r - idx) #차이를 구할때마다 절댓값을 취해야함
print(result)