#두개의 원소의 합이 100을 되는지
people = [70,50,80,50]
limit = 100

def solution(people,limit):
    people.sort() #몸무게 순서대로 [50,50,70,80]
    left,right = 0 ,len(people)-1
    count = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1 #[50 - 70]
        right -= 1 #[50 - 80, 50 - 70 ,50 -50] [50 - 70,50-80], [70,80]
        count += 1
    return count
print(solution(people,limit))