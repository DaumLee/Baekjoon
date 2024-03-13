from collections import deque


def spread(vrs):
    q = deque(vrs)
    v = [[0] * N for _ in range(N)]
    # 최초 방문 표시
    for vi, vj in vrs:
        v[vi][vj] = 1

    safe_cnt = safe
    time = 0
    while q:
        ci, cj = q.popleft()
        # 바이러스만 남았으면
        if not safe_cnt:
            break
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1
                time = max(time, v[ni][nj])
                # 안전 영역을 바이러스로 채웠으면
                if arr[ni][nj] != 2:
                    safe_cnt -= 1

    for i in range(N):
        for j in range(N):
            # 벽이 아닌데 방문한 적 없으면 불가능
            if arr[i][j] == 0 and not v[i][j]:
                return -1
    return time-1


def combinations(n, lst):
    global ans

    if len(lst) == M:
        t = spread(lst)
        # 지금 불가능인데, 정답이 나온 적 없으면
        if t == -1 and ans == 10e6:
            ans = -1
        # 정답이 지금 시간보다 더 걸렸으면
        elif t != -1 and ans > t:
            ans = t
        # 기존에는 불가능이었으나 정답을 찾았다면
        elif ans == -1 and t >= 0:
            ans = t
        return
    if n == len(virus):
        return

    for i in range(n+1, len(virus)):
        combinations(i, lst+[virus[i]])


N, M = map(int, input().split())
arr = []
virus = []
# 빈칸(0) 개수
safe = 0
for i in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)
    for j in range(N):
        if lst[j] == 2:
            virus.append((i, j))
        if lst[j] == 0:
            safe += 1

# 빈 칸이 없으면
if not safe:
    print(0)
else:
    ans = 10e6
    combinations(-1, [])
    print(ans)