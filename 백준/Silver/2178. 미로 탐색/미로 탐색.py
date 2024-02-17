def bfs(si, sj):
    v[si][sj] = 1
    q = [[si, sj]]
    length = len(q)
    depth = 1
    while q:
        ci, cj = q.pop(0)
        length -= 1
        if length < 0:
            length = len(q)
            depth += 1
        if ci == N-1 and cj == M-1:
            return depth
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and graph[ni][nj] == '1':
                q.append([ni, nj])
                v[ni][nj] = 1


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
v = [[0] * M for _ in range(N)]
di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)

print(bfs(0, 0))