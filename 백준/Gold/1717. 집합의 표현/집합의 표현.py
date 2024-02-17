import sys
input = sys.stdin.readline


def find(v):
    if v != p[v]:
        p[v] = find(p[v])
    return p[v]


def union(a, b):
    p[find(b)] = find(a)


N, M = map(int, input().split())
p = [i for i in range(N+1)]
for _ in range(M):
    cond, a, b = map(int, input().split())
    if cond:
        ans = 'YES' if find(a) == find(b) else 'NO'
        print(ans)
    else:
        union(a, b)