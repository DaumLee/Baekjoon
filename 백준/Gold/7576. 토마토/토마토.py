from collections import deque


def bfs(start):
    q = deque(start)
    v = [[0] * M for _ in range(N)]

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and graph[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return v

M, N = map(int, input().split())
graph = []
start = []
mx = 0

for i in range(N):
    lst = list(map(int, input().split()))
    graph.append(lst)
    for j in range(M):
        if lst[j] == 1:
            start.append((i, j))

ans = bfs(start)

for i in range(N):
    for j in range(M):
        if not ans[i][j] and not graph[i][j]:
            print(-1)
            exit(0)
        mx = max(mx, ans[i][j])

print(mx)