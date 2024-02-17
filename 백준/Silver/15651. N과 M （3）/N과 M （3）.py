def solve(n, temp):
    if n == M:
        print(*temp)
        return

    for i in range(N):
        solve(n+1, temp+[lst[i]])


N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]

solve(0, [])