import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력 받아
n = int(input())
tree = dict()
for _ in range(n):
    line = input().strip()
    if not line:
        continue
    root,child,weight = map(int,line.split())
    if not root in tree:
        tree[root] = []
    if child not in tree:
        tree[child] = []
    tree[root].append((child,weight))
    tree[child].append((root,weight))

visited_A = [False] * (n+1)
def find_A(root,weight):
    visited_A[root] = True
    max_length = weight
    farthest_node = root
    for c,w in tree.get(root,[]):
        if not visited_A[c]:
            child_length,child_node  = find_A(c,weight+w)
            # #최대거리 갱신
            #max_length = max(max_length,find_A(c,w+weight))
            if max_length < child_length:
                max_length = child_length
                farthest_node = child_node
    return max_length, farthest_node


_,end_node = find_A(1,0)
visited_B = [False] * (n+1)

def find_B(start):
    q = deque()
    q.append((start,0))
    visited_B[start] = True
    max_distance= 0
    while q:
        n,d = q.popleft()
        if d > max_distance:
            max_distance= d
        for ch,we in tree.get(n,[]):
            if not visited_B[ch]:
                visited_B[ch] =True
                q.append((ch,we+d))
    return max_distance
        

print(find_B(end_node))
