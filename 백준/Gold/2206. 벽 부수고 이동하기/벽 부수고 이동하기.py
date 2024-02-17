from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = [1, 0]

    while q:
        ci, cj = q.popleft()
        # if (ci, cj) == (N-1, M-1):
        #     return v[ci][cj][0]
        for di, dj in ((1, 0), (0, 1), (0, -1), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and (not v[ni][nj][0] or v[ni][nj][1] > v[ci][cj][1]):
                if ni == N-1 and nj == M-1:
                    return v[ci][cj][0] + 1
                if graph[ni][nj] == '1':
                    if v[ci][cj][1] == 1:
                        continue
                    v[ni][nj] = [v[ci][cj][0] + 1, v[ci][cj][1] + 1]
                else:
                    v[ni][nj] = [v[ci][cj][0] + 1, v[ci][cj][1]]
                q.append((ni, nj))
    return -1


N, M = map(int, input().split())

graph = [input() for _ in range(N)]
v = [[[0, 2] for j in range(M)] for i in range(N)]

if N == M == 1:
    print(1)
else:
    print(bfs(0, 0))