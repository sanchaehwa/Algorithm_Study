food = [1,3,4,6]
def solution(food):
    food_total = []
    food_1 = []
    food_2 = []
    water = []
    answer = []
    for idx,i in enumerate(food):
        food_total.extend([idx]*i)
    for i in set(food_total):
        a = food_total.count(i)
        if i >0 and a % 2 != 0:
                food_total.remove(i)
        if food_total.count(i) % 2 == 0:
                food_1.extend([i] * (food_total.count(i)//2))
        else:
            water.append(i)
    print(food_1)
    food_2 = food_1[::-1]
    answer = []
    answer.extend(food_1)
    answer.extend(water)
    answer.extend(food_2)
    return "".join(map(str,answer))
print(solution(food))