def dfs(start):
    visited = []
    stk = [start]

    while stk:
        v = stk.pop()
        if v not in visited:
            visited.append(v)
            if v <= V:
                stk.extend(graph[v])
    return len(visited)-1


V = int(input())
E = int(input())
graph = [list() for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(dfs(1))