from collections import deque


def bfs(si, sj):
    q = deque([(si, sj)])
    mx = 1
    while q:
        ci, cj = q.popleft()
        if v[ci][cj] > mx:
            mx = v[ci][cj] -1
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and graph[ni][nj] == 'L':
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))

    ans.append(mx)


N, M = map(int, input().split())
graph = []
start = []
for i in range(N):
    lst = input()
    graph.append(lst)
    for j in range(M):
        if lst[j] == 'L':
            start.append((i, j))
ans = []

for si, sj in start:
    v = [[0] * M for i in range(N)]
    v[si][sj] = 1
    bfs(si, sj)

print(max(ans))