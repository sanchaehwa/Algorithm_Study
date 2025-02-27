arr = []
row = list(map(int, input().split()))
arr.append(row)

# 행렬 크기 저장
x = arr[0][0]  # N (행 개수)
y = arr[0][1]  # M (열 개수)

# 행렬 A 입력
for _ in range(x):
    arr.append(list(map(int, input().split())))

number_indexing1 = arr[1:x+1]  # 행렬 A 추출
number_indexing2 = []

# 행렬 B 입력
for _ in range(x):
    number_indexing2.append(list(map(int, input().split())))

# 행렬 A와 B를 더한 결과 저장
result = []
for i in range(x):  # N번 반복
    answer = []  # 매 루프마다 초기화
    for j in range(y):  # M번 반복
        sum_number = number_indexing1[i][j] + number_indexing2[i][j]
        answer.append(sum_number)
    result.append(answer)

# 행렬 출력 (각 원소를 공백으로 구분)
for row in result:
    print(" ".join(map(str, row)))  # 리스트를 문자열로 변환하여 출력