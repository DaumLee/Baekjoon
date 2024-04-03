def move():
    dlst = [[list() for _ in range(N)] for _ in range(N)]
    speed = [[0] * N for _ in range(N)]
    cnt = [[0] * N for _ in range(N)]
    sm = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                for item in arr[i][j]:
                    m, s, d = item
                    di, dj = delta[d]
                    ni, nj = (i+di*s)%N, (j+dj*s)%N
                    sm[ni][nj] += m
                    speed[ni][nj] += s
                    cnt[ni][nj] += 1
                    dlst[ni][nj].append(d)
    nxt = [[list() for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if cnt[i][j]:
                if cnt[i][j] == 1:
                    nxt[i][j].append((sm[i][j], speed[i][j], dlst[i][j][0]))
                else:
                    std = (dlst[i][j][0])%2
                    flag = 0
                    for k in dlst[i][j][1:]:
                        if k%2 != std:
                            flag = 1
                            break
                    # 대각선 방향 확산
                    if flag:
                        m = sm[i][j] // 5
                        if not m:
                            continue
                        s = speed[i][j] // cnt[i][j]
                        for d in range(1, 8, 2):
                            di, dj = delta[d]
                            ni, nj = (i+di)%N, (j+dj)%N
                            nxt[i][j].append((m, s, d))
                    else:
                        m = sm[i][j] // 5
                        if not m:
                            continue
                        s = speed[i][j] // cnt[i][j]
                        for d in range(0, 7, 2):
                            di, dj = delta[d]
                            ni, nj = (i+di)%N, (j+dj)%N
                            nxt[i][j].append((m, s, d))
    return nxt


N, M, K = map(int, input().split())
delta = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
arr = [[list() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    si, sj, m, s, d = map(int, input().split())
    arr[si-1][sj-1].append((m, s, d))

for _ in range(K):
    arr = move()
ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            for item in arr[i][j]:
                ans += item[0]
print(ans)