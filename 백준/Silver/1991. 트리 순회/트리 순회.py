import sys
input = sys.stdin.readline
'''
전위 순회 : root -> left -> right
중위 순회 : left -> root -> right
후위 순회 : left -> right -> root

A - root
B - left 
C - right
'''

tree = {}

#이진 트리 노드의 개수 
N = int(input())
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left,right]

#전위 root -> left -> right
def preorder(root):
    if root != '.':
        print(root, end='') #root
        preorder(tree[root][0]) #left
        preorder(tree[root][1]) #right

#left -> root -> right
def inorder(root):
    if root != '.':
        inorder(tree[root][0]) #left
        print(root, end='')
        inorder(tree[root][1]) #right

def postorder(root):
    if root != '.':
        postorder(tree[root][0]) #left
        postorder(tree[root][1]) #right
        print(root, end='')

#항상 A가 루트 노드가 된다
preorder('A')
print()
inorder('A')
print()
postorder('A')
