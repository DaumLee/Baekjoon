from collections import deque

def dfs(s):
    d.append(s)
    v[s] = 1
    for next in sorted(graph[s]):
        if not v[next]:
            v[next] = 1
            dfs(next)

def bfs(s):
    v = [0] * (V + 1)
    q = deque()
    v[s] = 1
    q.append(s)
    b.append(s)

    while q:
        c = q.popleft()
        for next in sorted(graph[c]):
            if not v[next]:
                q.append(next)
                v[next] = 1
                b.append(next)


V, E, S = map(int, input().split())
graph = [[] for i in range(V+1)]
v = [0] * (V+1)
d = []
b = []

for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(S)
print(*d)
bfs(S)
print(*b)