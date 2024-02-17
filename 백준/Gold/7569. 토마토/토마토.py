from collections import deque

def bfs(s):
    q = deque(start)

    while q:
        ci, cj, ck = q.popleft()
        for di, dj, dk in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            ni, nj, nk = ci+di, cj+dj, ck+dk
            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and not v[ni][nj][nk] and not graph[ni][nj][nk]:
                v[ni][nj][nk] = v[ci][cj][ck] + 1
                q.append((ni, nj, nk))

    return v


M, N, H = map(int, input().split())
v = [[[0 for k in range(M)] for j in range(N)] for i in range(H)]
graph = [[list(map(int, input().split())) for j in range(N)] for i in range(H)]
start = []

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                start.append((i, j, k))
                v[i][j][k] = 1

ans = bfs(start)
flag = 0
mx = 0

for i in range(H):
    if flag:
        break
    for j in range(N):
        if flag:
            break
        for k in range(M):
            mx = max(mx, v[i][j][k])
            if v[i][j][k] == 0 and not graph[i][j][k]:
                print(-1)
                flag = 1
                break

if not flag:
    print(mx-1)