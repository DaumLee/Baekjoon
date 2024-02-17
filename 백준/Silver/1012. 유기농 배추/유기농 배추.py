import sys
sys.setrecursionlimit(10000)

def dfs(i, j):
    v[i][j] = 1

    for dy, dx in d:
        ny = i + dy
        nx = j + dx
        if 0 <= ny < N and 0 <= nx < M:
            if v[ny][nx] == 0:
                if arr[ny][nx] == 1:
                    dfs(ny, nx)

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for j in range(N)]

    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1

    v = [[0] * M for j in range(N)]
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and v[i][j] == 0:
                dfs(i, j)
                cnt += 1

    print(cnt)