#arr = [10]
def solution(arr):
    #if len(arr) > 0:
    min_number = min(arr)
        #print(min_number)
    arr.remove(min_number)
    #    return arr
    return arr if len(arr)>0 else [-1]
#print(solution(arr))