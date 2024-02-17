from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    temp = []

    while q:
        ci, cj = q.popleft()
        if graph[ci][cj] == graph[si][sj]:
            temp.append((ci, cj))
        if v[ci][cj] > 1:
            continue
        for di, dj in ((-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                if graph[ni][nj] > graph[si][sj] and v[ci][cj] <= 1:
                    return 0
                elif graph[ni][nj] == graph[ci][cj]:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj]
                else:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
    ans.extend(temp)
    return 1


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
ans = []

for i in range(N):
    for j in range(M):
        if graph[i][j] and (i, j) not in ans:
            cnt += bfs(i, j)

print(cnt)