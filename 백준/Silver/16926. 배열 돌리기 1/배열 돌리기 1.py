def rotate():
    nxt = [[0] * M for _ in range(N)]
    ci = cj = 0
    d = 0
    flag = 0
    cnt = 0
    while True:
        if cnt == N*M: break
        di, dj = delta[d]
        ni, nj = ci+di, cj+dj
        if 0 <= ni < N and 0 <= nj < M:
            if nxt[ni][nj] and d == 0 and not flag:
                ci, cj = ci+1, cj+1
                flag = 1
                continue
            elif nxt[ni][nj]:
                flag = 0
                d = (d+1)%4
                continue
            nxt[ni][nj] = arr[ci][cj]
            ci, cj = ni, nj
            cnt += 1
        else:
            d = (d+1)%4
            flag = 0
    return nxt


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
for _ in range(R):
    arr = rotate()
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=' ')
    print()