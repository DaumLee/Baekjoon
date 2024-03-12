from collections import deque


def bfs(si, sj, t):
    q = deque([(si, sj)])
    cnt = 1
    sm = arr[si][sj]

    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            # 국경선을 열 수 있으면
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and L <= abs(arr[ci][cj]-arr[ni][nj]) <= R:
                cnt += 1
                sm += arr[ni][nj]
                v[ni][nj] = t
                q.append((ni, nj))
                nlst[t].append((ni, nj))
    return sm, cnt


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = ((-1, 0), (0, -1), (0, 1), (1, 0))
time = 0
dct = dict()

while time <= 2000:
    t = 0
    v = [[0] * N for _ in range(N)]
    nlst = dict()
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                t += 1
                v[i][j] = t
                nlst[t] = [(i, j)]
                dct[t] = bfs(i, j, t)

    # 국경선을 열 수 없으면
    if t == N**2:
        break
    for n in range(1, t+1):
        sm, cnt = dct[n]
        for i, j in nlst[n]:
            arr[i][j] = sm//cnt
    time += 1

print(time)