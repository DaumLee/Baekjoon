from collections import deque


def check(si, sj):
    q = deque([(si, sj)])
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and arr[ni][nj] != 'G':
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1
    return v


N, M = map(int, input().split())
arr = []
for i in range(N):
    lst = list(input().strip())
    for j in range(M):
        if lst[j] == 'A':
            fi, fj = i, j
        elif lst[j] == 'B':
            si, sj = i, j
    arr.append(lst)

if (fi+fj)%2 != (si+sj)%2:
    print(-1)
    exit(0)

if si == 0 and sj < M-1: sd = 0
elif sj == M-1 and si < N-1: sd = 1
elif si == N-1 and sj > 0: sd = 2
else: sd = 3

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
v = check(fi, fj)

L = 2 * (N + M - 2)
MAX = N*M
mn = MAX
for t in range(L):
    if v[si][sj]:
        d = v[si][sj]-1
        if t >= d:
            mn = min(mn, t)
        else:
            mn = min(mn, t + ((d-t+L-1)//L)*L)
    di, dj = delta[sd]
    ni, nj = si+di, sj+dj
    if 0 <= ni < N and 0 <= nj < M:
        si, sj = ni, nj
    else:
        sd = (sd+1)%4
        di, dj = delta[sd]
        si, sj = si+di, sj+dj

if mn == MAX:
    print(-1)
else:
    print(mn)