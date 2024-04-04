def move(si, sj):
    for i in range(4):
        for j in range(4):
            if arr[i][j]:
                for d in arr[i][j]:
                    for _ in range(8):
                        di, dj = delta[d]
                        ni, nj = i+di, j+dj
                        if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (si, sj) and not blocked[ni][nj]:
                            nxt[ni][nj].append(d)
                            break
                        else:
                            d = (d-1)%8
                    else:
                        nxt[i][j].append(d)


def counting(ci, cj, dlst):
    score = 0
    r = []
    for d in dlst:
        di, dj = p_delta[d]
        ni, nj = ci+di, cj+dj
        if not (0 <= ni < 4 and 0 <= nj < 4): return -1
        if nxt[ni][nj] and (ni, nj) not in r:
            score += len(nxt[ni][nj])
        r.append((ni, nj))
        ci, cj = ni, nj
    return score


def play(si, sj, route):
    ei, ej = si, sj
    for d in route:
        di, dj = p_delta[d]
        ni, nj = ei+di, ej+dj
        if nxt[ni][nj]:
            nxt[ni][nj] = []
            blocked[ni][nj] = 2
        ei, ej = ni, nj
    return ei, ej


M, T = map(int, input().split())
delta = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
p_delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
arr = [[list() for _ in range(4)] for _ in range(4)]
for _ in range(M):
    i, j, d = map(lambda x: int(x)-1, input().split())
    arr[i][j].append(d)
si, sj = map(lambda x: int(x)-1, input().split())
blocked = [[0] * 4 for _ in range(4)]
for time in range(1, T+1):
    nxt = [[list() for _ in range(4)] for _ in range(4)]
    move(si, sj)
    for i in range(4):
        for j in range(4):
            if blocked[i][j]:
                blocked[i][j] -= 1
    mx = -1
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                cnt = counting(si, sj, [d1, d2, d3])
                if cnt > mx:
                    mx = cnt
                    route = [d1, d2, d3]
    si, sj = play(si, sj, route)
    for i in range(4):
        for j in range(4):
            arr[i][j] += nxt[i][j]
    continue
ans = 0
for i in range(4):
    for j in range(4):
        if arr[i][j]: ans += len(arr[i][j])
print(ans)