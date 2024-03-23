from collections import deque

def grouping(si, sj, n):
    q = deque([(si, sj)])

    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and not c[ni][nj]:
                c[ni][nj] = n
                q.append((ni, nj))

def bridge(si, sj):
    global mn
    num = c[si][sj]
    q = deque([(si, sj)])

    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj]:
                if c[ni][nj] == num:
                    continue
                # 바다면 다리를 놓음
                elif not c[ni][nj]:
                    v[ni][nj] = v[ci][cj]+1
                    q.append((ni, nj))
                # 다리 완공
                else:
                    mn = min(v[ci][cj]-1, mn)
                    return

N = int(input())
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
arr = [list(map(int, input().split())) for _ in range(N)]
c = [[0] * N for _ in range(N)]
num = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] and not c[i][j]:
            c[i][j] = num
            grouping(i, j, num)
            num += 1

mn = N**2
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            bridge(i, j)
print(mn)