def solve(n, temp, idx):
    global ans
    if n == N:
        sm = 0
        for i in range(N-1):
            sm += abs(temp[i]-temp[i+1])
        ans = max(sm, ans)
        return

    for i in range(N):
        if i not in idx:
            solve(n+1, temp+[lst[i]], idx+[i])


N = int(input())
lst = list(map(int, input().split()))
ans = 0
solve(0, [], [])
print(ans)