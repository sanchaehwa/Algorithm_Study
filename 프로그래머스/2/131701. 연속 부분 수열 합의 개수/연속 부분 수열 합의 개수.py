
def solution(elements):
    answer = set()

    for i in range(len(elements)):
        sequence_sum = 0;
        for j in range(i, len(elements)+i):
            sequence_sum += elements[j%len(elements)]
            answer.add(sequence_sum)
    return len(answer)