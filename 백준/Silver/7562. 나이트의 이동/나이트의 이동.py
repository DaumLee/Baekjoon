def bfs(si, sj, ei, ej):
    q = [(si, sj)]
    v = [[0] * l for _ in range(l)]
    
    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (ei, ej):
            return v[ci][cj]
        for di, dj in ((-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < l and 0 <= nj < l and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

T = int(input())

for _ in range(T):
    l = int(input())

    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    ans = bfs(si, sj, ei, ej)

    print(ans)