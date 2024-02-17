def solve(n, s, temp):
    global cnt

    if sum(temp) == S:
        if temp:
            cnt += 1

    if n == N:
        return

    for i in range(s, N):
        solve(n+1, i+1, temp+[lst[i]])


N, S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
solve(0, 0, [])
print(cnt)