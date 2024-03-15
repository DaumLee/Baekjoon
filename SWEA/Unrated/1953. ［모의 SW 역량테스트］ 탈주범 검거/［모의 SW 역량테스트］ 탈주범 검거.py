from collections import deque

def linked(si, sj, ei, ej):
    dir = delta[arr[si][sj]]
    for di, dj in dir:
        ni, nj = si+di, sj+dj
        if ni == ei and nj == ej:
            return True
    return False

def bfs(si, sj, t):
    q = deque([(si, sj)])
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    cnt = 0

    while q:
        ci, cj = q.popleft()
        if v[ci][cj] == t:
            break
        for di, dj in delta[arr[ci][cj]]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and (not v[ni][nj] or v[ni][nj] > v[ci][cj]+1):
                if linked(ni, nj, ci, cj):
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj]+1

    for i in range(N):
        for j in range(M):
            if v[i][j]:
                cnt += 1
    return cnt

delta = {1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
         2: ((1, 0), (-1, 0)),
         3: ((0, 1), (0, -1)),
         4: ((-1, 0), (0, 1)),
         5: ((0, 1), (1, 0)),
         6: ((0, -1), (1, 0)),
         7: ((-1, 0), (0, -1))}

for tc in range(1, int(input())+1):
    N, M, si, sj, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(si, sj, l)
    print(f'#{tc} {ans}')