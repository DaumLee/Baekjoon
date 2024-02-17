from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    cnt = 0

    while q:
        ci, cj = q.popleft()
        if graph[ci][cj] == 'P':
            cnt += 1
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and graph[ni][nj] != 'X':
                q.append((ni, nj))
                v[ni][nj] = 1

    return cnt if cnt else 'TT'


N, M = map(int, input().split())
graph = [input() for _ in range(N)]
goal = []
cnt = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            si, sj = i, j
        elif graph[i][j] == 'P':
            goal.append((i, j))

print(bfs(si, sj))