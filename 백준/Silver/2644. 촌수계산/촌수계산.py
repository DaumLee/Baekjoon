def bfs(head, goal):
    v[head] = 1
    q = graph[head]
    length = len(q)
    depth = 1

    while q:
        next = q.pop(0)
        length -= 1
        if length < 0:
            depth += 1
            length = len(q)
        if next == goal:
            return depth
        if not v[next]:
            v[next] = 1
            q.extend(graph[next])
    return -1

n = int(input())
S, G = map(int, input().split())
m = int(input())
graph = [list() for _ in range(n+1)]
v = [0] * (n+1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(S, G))