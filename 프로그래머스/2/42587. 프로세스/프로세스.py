'''
1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
'''
from collections import deque
priorities = [2, 1, 3, 2]
# C D A B
location = 1
#가장 앞에있으면 0 / 두번째 있으면 1 / 2 / 3/ 4

#몇 번째로 실행이 되는지 

def solution(priorities, location):
    q = deque((i, j) for i, j in enumerate(priorities))
    answer = []
    while q:
        idx, num = q.popleft()
        if q and any(num < queue[1] for queue in q):
            q.append((idx,num))
        else:
            answer.append((idx,num))

    for i in answer:
        if i[0] == location:
            return answer.index(i) + 1
print(solution(priorities,location))