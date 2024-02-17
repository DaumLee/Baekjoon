def dfs(ci, cj, step):
    global cnt
    v[ci][cj] = 1

    if step == K and ci == 0 and cj == M-1:
        cnt += 1
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci+di, cj+dj
        if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and graph[ni][nj] != 'T' and v[ci][cj] <= K-1:
            v[ni][nj] = 1
            dfs(ni, nj, step+1)
            v[ni][nj] = 0


N, M, K = map(int, input().split())
graph = [input() for _ in range(N)]
cnt = 0
v = [[0] * M for _ in range(N)]

dfs(N-1, 0, 1)

print(cnt)