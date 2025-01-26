#arr1 =[[1],[2]]	
#arr2 =[[3],[4]]	
def solution(arr1,arr2):
   # answer = [[]]
    #result = []
    answer = []
    for idx1,row in enumerate(arr1):
            result_row = []
            for idx2, value in enumerate(row):
                row_sum = value + arr2[idx1][idx2]
                result_row.append(row_sum)
            answer.append(result_row)

  #  print(answer)
              
    return answer
#print(solution(arr1,arr2))