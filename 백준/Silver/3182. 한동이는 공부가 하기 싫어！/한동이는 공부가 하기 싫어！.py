def dfs(start):
    dist = 0
    nxt = lst[start]-1
    while not v[nxt]:
        v[nxt] = 1
        nxt = lst[nxt]-1
        dist += 1
    return dist


N = int(input())
lst = list(int(input()) for _ in range(N))
mx = 0
ans = 1

for num in range(N):
    v = [0] * N
    v[num] = 1
    cnt = dfs(num)
    if cnt > mx:
        mx = cnt
        ans = num+1

print(ans)