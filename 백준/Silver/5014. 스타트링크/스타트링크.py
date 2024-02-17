from collections import deque

def bfs(S, G):
    q = deque()
    v = [0] * (F+1)
    v[S] = 1
    q.append(S)

    while q:
        c = q.popleft()
        for d in (U, -D):
            n = c + d
            if n > F:
                continue
            if n == G:
                return v[c]
            if 0 < n and not v[n]:
                v[n] = v[c] + 1
                q.append(n)
    return "use the stairs"


F, S, G, U, D = map(int, input().split())

if S == G:
    print(0)
else:
    print(bfs(S, G))