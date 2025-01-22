# 이진수 변환 함수
def replace_binarynumber(n, number):
    binary_array = []

    for i in number:
        binary_list = []
        while i != 0:
            binary_list.append(i % 2)
            i = i // 2
        binary_list.reverse()
        while len(binary_list) < n:
            binary_list.insert(0, 0)
        binary_array.append(binary_list)

    return binary_array

# 문자 변환 함수 
def replace_char(binary_array):
    list_char = []

    for i in binary_array:
        s = ""
        for j in i:
            if j == 0:
                s += " "
            else:
                s += "#"
        list_char.append(s)

    return list_char

def solution(n, arr1, arr2):
    result = []
    replace_binarynumber_arr1 = replace_binarynumber(n, arr1)  # 'n' 추가
    replace_binarynumber_arr2 = replace_binarynumber(n, arr2)  # 'n' 추가

    for row1, row2 in zip(replace_binarynumber_arr1, replace_binarynumber_arr2):
        merged_row = ""
        for bit1, bit2 in zip(row1, row2):
            if bit1 == 1 or bit2 == 1:
                merged_row += "#"
            else:
                merged_row += " "
        result.append(merged_row)

    return result

