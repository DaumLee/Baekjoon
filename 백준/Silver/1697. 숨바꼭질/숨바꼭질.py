import sys
from collections import deque


def bfs(s, e):

    if s > e:
        return s-e
    elif s == e:
        return 0

    q = deque()
    v = set()
    q.append((s, 0))
    v.add(s)

    while q:
        c = q.popleft()
        next = (c[0]-1, c[0]+1, c[0]*2)
        if e in next:
            return c[1] + 1
        for n in next:
            if n not in v and n <= 2*e+1:
                q.append((n, c[1]+1))
                v.add(n)
    return -1


N, K = map(int, sys.stdin.readline().split())

print(bfs(N, K))