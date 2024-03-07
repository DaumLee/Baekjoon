from collections import deque
from itertools import combinations


def check(a):
    q = deque([a[0]])
    v = [0]*(N+1)
    v[a[0]] = 1
    cnt = 1

    while q:
        cur = q.popleft()
        for nxt in dct[cur]:
            if nxt not in a:
                continue
            if v[nxt]:
                continue
            q.append(nxt)
            v[nxt] = 1
            cnt += 1

    if cnt == len(a):
        return True
    else:
        return False


def cal(a):
    global ans

    sm_a = sm_b = 0
    for i in range(1, N+1):
        if i in a:
            sm_a += lst[i-1]
        else:
            sm_b += lst[i-1]
    ans = min(ans, abs(sm_a-sm_b))


N = int(input())
lst = list(map(int, input().split()))
dct = {k: set() for k in range(1, N+1)}
ans = 10e6

for i in range(1, N+1):
    n, *adj = map(int, input().split())
    for j in adj:
        dct[i].add(j)

for n in range(1, N//2+1):
    for a in combinations(range(1, N+1), n):
        if not check(a):
            continue
        b = []
        for i in range(1, N+1):
            if i not in a:
                b.append(i)
        if not check(b):
            continue
        cal(a)

if ans == 10e6:
    print(-1)
else:
    print(ans)