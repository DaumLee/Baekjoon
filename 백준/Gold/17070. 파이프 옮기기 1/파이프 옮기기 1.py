def dfs(ci, cj, d):
    global ans

    if ci == N-1 and cj == N-1:
        ans += 1
        return

    if d == 0 or d == 2:
        if not arr[ci][cj+1]:
            dfs(ci, cj+1, 0)
    if d == 1 or d == 2:
        if not arr[ci+1][cj]:
            dfs(ci+1, cj, 1)
    if not arr[ci+1][cj+1] and not arr[ci+1][cj] and not arr[ci][cj+1]:
        dfs(ci+1, cj+1, 2)


N = int(input())
arr = [list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (N+1)]
ans = 0
dfs(0, 1, 0)
print(ans)