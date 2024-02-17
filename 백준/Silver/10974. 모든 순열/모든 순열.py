def solve(n, temp):
    if n == N:
        print(*temp)
        return

    for i in range(N):
        if lst[i] in temp:
            continue
        solve(n+1, temp+[lst[i]])


N = int(input())
lst = [i for i in range(1, N+1)]
solve(0, [])