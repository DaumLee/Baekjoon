from collections import deque


def bfs(s, fire):
    q = deque(fire)
    q.append(s)
    v = [[0] * M for _ in range(N)]

    while q:
        ci, cj = q.popleft()
        if graph[ci][cj] == 'J' and (ci == 0 or ci == N - 1 or cj == 0 or cj == M - 1):
            graph[ci][cj] = '*'
            return v[ci][cj] + 1
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                if graph[ci][cj] == 'F' and graph[ni][nj] == '.':
                    graph[ni][nj] = 'F'
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni, nj))
                if graph[ci][cj] == 'J' and graph[ni][nj] == '.':
                    graph[ni][nj] = 'J'
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni, nj))
    return 'IMPOSSIBLE'


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
s = (0, 0)
fire = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'J':
            s = i, j
        elif graph[i][j] == 'F':
            fire.append((i, j))

print(bfs(s, fire))