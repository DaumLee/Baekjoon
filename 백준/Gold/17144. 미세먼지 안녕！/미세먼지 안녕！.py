def spread():
    nxt = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt = 0
                for di, dj in delta:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in hos:
                        cnt += 1
                        nxt[ni][nj] += arr[i][j]//5
                nxt[i][j] += arr[i][j]-((arr[i][j]//5) * cnt)
    return nxt


def upside(start, cd):
    ci, cj = start
    while True:
        di, dj = delta[cd]
        ni, nj = ci+di, cj+dj
        if (ni, nj) == start:
            break
        if 0 <= ni <= start[0] and 0 <= nj < M:
            arr[ci][cj], arr[ni][nj] = arr[ni][nj], arr[ci][cj]
            ci, cj = ni, nj
        else:
            cd = (cd-1)%4
    arr[start[0]][start[1]] = 0


def downside(start, cd):
    ci, cj = start
    while True:
        di, dj = delta[cd]
        ni, nj = ci+di, cj+dj
        if (ni, nj) == start:
            break
        if start[0] <= ni < N and 0 <= nj < M:
            arr[ci][cj], arr[ni][nj] = arr[ni][nj], arr[ci][cj]
            ci, cj = ni, nj
        else:
            cd = (cd+1)%4
    arr[start[0]][start[1]] = 0


N, M, T = map(int, input().split())
arr = []
hos = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] == -1:
            hos.append((i, j))
            lst[j] = 0
    arr.append(lst)

delta = ((0, 1), (-1, 0), (0, -1), (1, 0))
for _ in range(T):
    arr = spread()
    upside(hos[0], 1)
    downside(hos[1], 3)
ans = 0
for i in range(N):
    for j in range(M):
        ans += arr[i][j]
print(ans)