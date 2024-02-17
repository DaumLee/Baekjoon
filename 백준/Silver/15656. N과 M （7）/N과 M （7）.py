def solve(n, temp):
    if n == M:
        print(*temp)
        return

    for i in range(N):
        solve(n+1, temp+[lst[i]])


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

solve(0, [])