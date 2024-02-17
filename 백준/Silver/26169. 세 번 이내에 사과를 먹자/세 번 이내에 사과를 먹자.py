def solve(n, ci, cj, cnt):
    global ans
    if n > 3:
        return
    if n >= 2 and cnt >= 2:
        ans = 1
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci+di, cj+dj
        if 0 <= ni < 5 and 0 <= nj < 5 and not v[ni][nj] and graph[ni][nj] != -1:
            v[ni][nj] = 1
            if graph[ni][nj] == 1:
                solve(n+1, ni, nj, cnt+1)
            else:
                solve(n+1, ni, nj, cnt)
            v[ni][nj] = 0


graph = [list(map(int, input().split())) for _ in range(5)]
si, sj = map(int, input().split())
ans = 0
v = [[0] * 5 for _ in range(5)]
v[si][sj] = 1
solve(0, si, sj, 0)
print(ans)