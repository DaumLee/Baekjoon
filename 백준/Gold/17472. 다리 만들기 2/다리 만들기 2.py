from collections import deque

def find(v):
    if p[v] != v:
        p[v] = find(p[v])
    return p[v]

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        p[b] = a

def grouping(si, sj, n):
    q = deque([(si, sj)])

    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not c[ni][nj]:
                c[ni][nj] = n
                q.append((ni, nj))

def bridge(si, sj):
    num = c[si][sj]

    # 다리는 직선으로만
    for d in range(2):
        ci, cj = si, sj
        di, dj = delta[d]
        cnt = 0
        while True:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if c[ni][nj] == num:
                    break
                # 바다면 다리를 놓음
                elif not c[ni][nj]:
                    cnt += 1
                    ci, cj = ni, nj
                # 다리 완공
                else:
                    if cnt > 1:
                        edge.append((cnt, num, c[ni][nj]))
                    break
            else:
                break

def linked():
    for i in range(1, num):
        for j in range(i + 1, num):
            if find(i) == find(j):
                continue
            else:
                return False
    return True

N, M = map(int, input().split())
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
arr = [list(map(int, input().split())) for _ in range(N)]
c = [[0] * M for _ in range(N)]
num = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] and not c[i][j]:
            c[i][j] = num
            grouping(i, j, num)
            num += 1

edge = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            bridge(i, j)
edge.sort()

p = [i for i in range(num)]
ans = 0
for length, s, e in edge:
    if find(s) != find(e):
        ans += length
        union(s, e)

if linked():
    print(ans)
else:
    print(-1)