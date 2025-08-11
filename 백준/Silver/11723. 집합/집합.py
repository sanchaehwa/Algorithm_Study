import sys
input = sys.stdin.readline

M = int(input())
lst = set()
for _ in range(M):
    put = input().strip()
    spl = put.split(' ')
    if len(spl) == 1:
        cmd = spl[0]
    else:
        cmd,num = spl[0],int(spl[1])
    if cmd == "add":
        lst.add(num)
    if cmd == "check":
        # if num in lst:
        #     print(1)
        # else:
        #     print(0)
        print(1 if num in lst else 0)
    if cmd == "remove":
        lst.discard(num) #자동으로 넘어감
    if cmd == "toggle":
        if num in lst:
            lst.remove(num)
        else:
            lst.add(num)
    elif cmd == "all":
        lst = set(range(1,21))
    if cmd == "empty":
        lst.clear()