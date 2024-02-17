def solve(n, s, temp):
    if n == M:
        print(*temp)
        return

    for i in range(s, N):
        if lst[i] not in temp:
            solve(n+1, i+1, temp+[lst[i]])


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

solve(0, 0, [])