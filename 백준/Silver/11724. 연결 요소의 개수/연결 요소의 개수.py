def dfs(v):
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [0] * (V+1)
for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

cnt = 0
for i in range(1, V+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)