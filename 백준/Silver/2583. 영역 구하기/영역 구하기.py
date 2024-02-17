import sys
sys.setrecursionlimit(10000)


def dfs(i, j):
    v[i][j] = 1
    ans.append(1)

    for dy, dx in d:
        ny = i + dy
        nx = j + dx
        if 0 <= ny < M and 0 <= nx < N:
            if v[ny][nx] == 0:
                if arr[ny][nx] == 0:
                    dfs(ny, nx)


M, N, K = map(int, input().split())
arr = [[0] * N for j in range(M)]

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())

    for i in range(sy, ey):
        for j in range(sx, ex):
            arr[i][j] = 1

v = [[0] * N for j in range(M)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
ans = []
cnt = 0

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and v[i][j] == 0:
            dfs(i, j)
            ans.append(0)
            cnt += 1

ans.append(0)
area = []
sm = 0
for i in range(len(ans)-1):
    if ans[i] == 1 and ans[i+1] == 1:
        sm += 1
    elif ans[i] == 1 and ans[i+1] == 0:
        area.append(sm+1)
        sm = 0

print(cnt)
print(*sorted(area))