#순회 하면서, 각 숫자를 n길이만큼 이진수로 변환 array에 담아
#변환한 걸 또 순회하면서, 문자열로 변환하고 문자열을 answer append
#map1,2이니깐 함수 호출
#n = 5
#arr1 = [9, 20, 28, 18, 11]
#arr2 = [30, 1, 21, 17, 28]
def replace_binnumber(number, n):
    # 이진수 변환 
   # binary_array = []
    # for i in number:
    #     binary_list = []
    #     while i != 0:
    #         binary_list.append(i % 2)
    #         i = i // 2
    #     binary_list.reverse()
    #     while len(binary_list) < n:  # n 길이를 기준으로 왼쪽에 0 채움
    #         binary_list.insert(0, 0)
    #     binary_array.append(binary_list)
    binary_array = []
    for i in number:
        binary_str = bin(i)[2:]  # '0b' 제거 
        binary_str = binary_str.zfill(n)  # n 길이를 기준으로 왼쪽에 0 채움
        binary_list = [int(bit) for bit in binary_str]  # 문자열을 정수 리스트로 변환
        binary_array.append(binary_list)
   # return binary_array
   #문자 변환 
    list_char = []
    for i in binary_array:
        s = "".join("#" if bit else " " for bit in i)
        list_char.append(s)
    return list_char
    

# # 문자 변환 함수 (각 행을 문자열로 변환)
# def replace_char(binary_array):
#     list_char = []
#     for i in binary_array:
#         s = "".join("#" if bit else " " for bit in i)
#         list_char.append(s)
#     return list_char

def solution(n, arr1, arr2):
    # 이진수 변환 + 문자 변환
    replace_binnumber_arr1 = replace_binnumber(arr1, n)
    replace_binnumber_arr2 = replace_binnumber(arr2, n)

    # 두 배열을 비교해 결과 생성
    result = []
    for row1, row2 in zip(replace_binnumber_arr1,  replace_binnumber_arr2 ):
        p = ""
        for char1, char2 in zip(row1, row2):
            if char1 == "#" or char2 == "#":
                p += "#"
            else:
                p += " "
        result.append(p)

   # print(result)  
    return result
 
#print(solution(n, arr1, arr2))