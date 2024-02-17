from collections import deque


def bfs(s):
    q = deque()
    v = dict()
    q.append(s)
    v[s] = [s, 1]

    while q:
        c = q.popleft()
        for n in (c*2, c*10+1):
            if n == B:
                return v[c][1] + 1
            if n < B and n not in v:
                q.append(n)
                v[n] = [n, v[c][1] + 1]
    return -1


A, B = map(int, input().split())

print(bfs(A))