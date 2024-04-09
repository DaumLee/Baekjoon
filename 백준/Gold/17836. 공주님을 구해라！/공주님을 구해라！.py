from collections import deque

def bfs(si, sj):
    q = deque([(si, sj)])
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    ans = T+1
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (N-1, M-1): ans = min(ans, v[ci][cj]-1)
        if v[ci][cj]-1 > T: break
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and arr[ni][nj] != 1:
                v[ni][nj] = v[ci][cj]+1
                if arr[ni][nj] == 2:
                    ans = min(ans, v[ci][cj]+N-1-ni+M-1-nj)
                else:
                    q.append((ni, nj))
    return ans if ans <= T else 'Fail'

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs(0, 0))