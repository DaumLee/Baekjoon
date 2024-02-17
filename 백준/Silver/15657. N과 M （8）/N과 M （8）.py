def solve(n, s, temp):
    if n == M:
        print(*temp)
        return

    for i in range(s, N):
        solve(n+1, i, temp+[lst[i]])


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

solve(0, 0, [])