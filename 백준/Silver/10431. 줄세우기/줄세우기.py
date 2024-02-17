import sys

p = int(input())

for _ in range(p):
    t, *key = map(int, input().split())
    lst = [0] * 20
    cnt = 0
    for a in key:
        for i in range(20):
            if lst[i] == 0:
                lst[i] = a
                break
            if a > lst[i]:
                continue
            if a < lst[i]:
                lst.insert(i, a)
                lst.pop()
                cnt += (key.index(a) - i)
                break
    print(t, cnt)
