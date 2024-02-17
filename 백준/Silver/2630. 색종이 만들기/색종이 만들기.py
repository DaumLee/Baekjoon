def solve(si, sj, size):
    c = graph[si][sj]

    for i in range(si, si+size):
        for j in range(sj, sj+size):
            if graph[i][j] != c:
                solve(si, sj, size//2)
                solve(si, sj+size//2, size//2)
                solve(si+size//2, sj, size//2)
                solve(si+size//2, sj+size//2, size//2)
                return
    if c:
        ans[1] += 1
    else:
        ans[0] += 1

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]
solve(0, 0, N)
print(*ans, sep='\n')