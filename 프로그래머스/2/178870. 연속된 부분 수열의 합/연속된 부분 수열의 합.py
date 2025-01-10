#sequence = 	[1, 1, 1, 2, 3, 4, 5]
#k = 5
def solution(sequence, k):
    start = 0
    end = 0
    lower = len(sequence)
    answer = []
    sum = 0
    for end in range(len(sequence)):

        sum += sequence[end]

        while sum > k:
            sum -= sequence[start]
            start += 1

        if sum == k:
            # 2, 2, 2, 2, 2
            # k = 6
            if lower > end-start:
                lower = end-start 
                answer = [start,end]
        
    return answer
#print(solution(sequence, k))