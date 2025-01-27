a, b = map(int, input().strip().split(' '))
list_map = [['*'] * a for _ in range(b)]
result = [''.join(row)for row in list_map]
for row in result: print(row)
