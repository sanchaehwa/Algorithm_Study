import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]
tree = dict()

for line in nums:
    root = line[0]
    sub_num = line[1:-1] #첫번째 원소랑 마지막 원소는 제외
    lst = [tuple(sub_num[i:i+2]) for i in range(0,len(sub_num),2)]
    for child,weight in lst:
        tree.setdefault(root,[]).append((child,weight))
        tree.setdefault(child,[]).append((root,weight))
        
visited = [False] * (n+1)

# 5부터 시작
def find_node_A(root, weight):
    visited[root] = True
    maxWeight = weight
    farthest_node = root
    for N,W in tree.get(farthest_node,[]):
        if not visited[N]:
            a_weight, a_node = find_node_A(N,weight+W)
            #print(find_max_length(n,weight+w))
            if a_weight > maxWeight:
                maxWeight = a_weight
                farthest_node = a_node
    return maxWeight,farthest_node 

_, end_node = find_node_A(1,0)
visited_B = [False] * (n+1)
def find_node_B(start):
    q = deque()
    q.append((start,0)) # node / distance 
    visited_B[start] = True
    max_distance = 0
    while q:
        node,distance = q.popleft()
        if distance > max_distance:
            max_distance = distance
           # print(max_distance)
        for n,w in tree.get(node,[]):
           # print(n,w)
            if not visited_B[n]:
                visited_B[n] = True
                q.append((n,w+distance))
    return max_distance
print(find_node_B(end_node))




