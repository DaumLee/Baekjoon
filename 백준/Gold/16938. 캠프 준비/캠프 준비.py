def solve(n, idx, sm, mx, mn):
    global cnt

    if sm > R:
        return

    if n >= 2:
        if mx - mn >= X and sm >= L:
            cnt += 1

    for j in range(idx+1, N):
        solve(n+1, j, sm+lst[j], max(mx, lst[j]), min(mn, lst[j]))


N, L, R, X = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(N-1):
    solve(1, i, lst[i], lst[i], lst[i])
print(cnt)