from collections import deque

def find_enemy(si, sj):
    q = deque([(si, sj)])
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    cand = []
    flag = N**2*2
    while q:
        ci, cj = q.popleft()
        if v[ci][cj] > flag: break
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and arr[ni][nj] <= level:
                if arr[ni][nj] and arr[ni][nj] < level:
                    cand.append((ni, nj, v[ci][cj]))
                    flag = v[ci][cj]
                v[ni][nj] = v[ci][cj]+1
                q.append((ni, nj))
    if cand:
        cand.sort()
        return cand[0]
    return -1, -1, -1

N = int(input())
arr = []
for i in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)
    for j in range(N):
        if lst[j] == 9:
            si, sj = i, j
            lst[j] = 0
delta = ((-1, 0), (0, -1), (0, 1), (1, 0))
level = 2
ans = 0
eat = 0
while True:
    ei, ej, time = find_enemy(si, sj)
    if (ei, ej) == (-1, -1): break
    ans += time
    arr[ei][ej] = 0
    si, sj = ei, ej
    eat += 1
    if eat == level:
        level += 1
        eat = 0
print(ans)