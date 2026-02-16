'''
문제 : 상근이가 가지고 있는 카드 - 그 카드의 숫자 중 정수 M개 해당되는건 몇개인지

1. 숫자카드개수
2. 숫자카드에 적혀있는 정수
3. 정수 M개
4. 정수 숫자
'''
import sys
input = sys.stdin.readline
#상근이가 가지고 있는
N = int(input())
cards = sorted(list(map(int,input().split())))

#찾아야하는
M = int(input())
nums = list(map(int,input().split()))

target_nums_dict = dict()

for i,t in enumerate(nums):
    if t not in target_nums_dict:
        target_nums_dict[t] = []
    target_nums_dict[t].append(i)

target_nums = sorted(target_nums_dict.items())


answer = [0] * M

cards_point = 0
nums_point = 0



while cards_point < N and nums_point < len(target_nums):
    if cards[cards_point] < target_nums[nums_point][0]:
        cards_point += 1
    elif cards[cards_point] > target_nums[nums_point][0]:
        nums_point += 1
    else:
        lst = target_nums[nums_point][1]
        for l in lst:
            answer[l] = 1
        cards_point += 1
        nums_point += 1

print(' '.join(map(str,answer)))