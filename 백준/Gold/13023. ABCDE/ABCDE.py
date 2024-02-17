def solve(n, idx, next, tlst):
    global cnt
    
    if cnt:
        return
    
    if n == 5:
        cnt = 1
        return

    for i in next:
        if i not in tlst:
            solve(n+1, i, graph[i], tlst+[i])


N, M = map(int, input().split())
graph = [list() for _ in range(N)]
cnt = 0
for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(N):
    solve(1, i, graph[i], [i])
    if cnt:
        break

print(cnt)