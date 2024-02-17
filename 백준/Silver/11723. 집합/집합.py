import sys
input = sys.stdin.readline

M = int(input())
s = set()
for _ in range(M):
    order = input().split()
    if order[0] == 'add':
        if order[1] in s:
            continue
        s.add(order[1])
    elif order[0] == 'remove':
        if order[1] not in s:
            continue
        s.remove(order[1])
    elif order[0] == 'check':
        print(int(order[1] in s))
    elif order[0] == 'toggle':
        if order[1] in s:
            s.remove(order[1])
        else:
            s.add(order[1])
    elif order[0] == 'all':
        s = {str(i) for i in range(1, 21)}
    else:
        s = set()