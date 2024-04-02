def move(time):
    global cnt

    nxt = [[0] * N for _ in range(N)]
    for num in range(1, M+1):
        ci, cj = loc[num]
        if (ci, cj) == (-1, -1): continue
        d = dir[num]
        cani, canj = -1, -1
        cand = d
        for k in p[num][d]:
            di, dj = delta[k]
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N:
                if not v[ni][nj] or time-v[ni][nj][1] > K:
                    if nxt[ni][nj] and nxt[ni][nj] < num:
                        loc[num] = (-1, -1)
                        cnt -= 1
                    elif nxt[ni][nj]:
                        loc[nxt[ni][nj]] = (-1, -1)
                        loc[num] = (ni, nj)
                        nxt[ni][nj] = num
                        dir[num] = k
                        cnt -= 1
                    else:
                        loc[num] = (ni, nj)
                        nxt[ni][nj] = num
                        dir[num] = k
                    break
                elif v[ni][nj][0] == num and cani == -1:
                    cani, canj = ni, nj
                    cand = k
        else:
            if nxt[cani][canj] and nxt[cani][canj] < num:
                loc[num] = (-1, -1)
                cnt -= 1
            elif nxt[cani][canj]:
                loc[nxt[cani][canj]] = (-1, -1)
                loc[num] = (cani, canj)
                nxt[cani][canj] = num
                dir[num] = cand
                cnt -= 1
            else:
                loc[num] = (cani, canj)
                nxt[cani][canj] = num
                dir[num] = cand

    for i in range(N):
        for j in range(N):
            if nxt[i][j]:
                v[i][j] = (nxt[i][j], time)
    return nxt


N, M, K = map(int, input().split())
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
v = [[0] * N for _ in range(N)]
arr = []
loc = dict()
cnt = 0
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j]:
            cnt += 1
            loc[lst[j]] = (i, j)
            v[i][j] = (lst[j], 0)
    arr.append(lst)
dir = dict()
lst = list(map(int, input().split()))
for num, i in enumerate(lst):
    dir[num+1] = i-1
p = [[list() for _ in range(4)] for _ in range(M+1)]
for i in range(1, M+1):
    for j in range(4):
        p[i][j] = list(map(lambda x: int(x)-1, input().split()))
for time in range(1, 1002):
    arr = move(time)
    if cnt == 1:
        break
if time == 1001:
    print(-1)
else:
    print(time)