from collections import deque
import sys
input = sys.stdin.readline

def bfs(si, sj):
    q = deque([(si, sj, 0, 0)])
    v = [[[-1] * (K+1) for j in range(M)] for i in range(N)]
    v[si][sj][0] = 0

    while q:
        ci, cj, time, cnt = q.popleft()
        if ci == N-1 and cj == M-1:
            return v[ci][cj][cnt]
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and (v[ni][nj][cnt] == -1 or v[ni][nj][cnt] > time+1):
                v[ni][nj][cnt] = time+1
                q.append((ni, nj, time+1, cnt))
        if cnt < K:
            for hi, hj in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
                ni, nj = ci+hi, cj+hj
                if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and (v[ni][nj][cnt+1] == -1 or v[ni][nj][cnt+1] > time+1):
                    v[ni][nj][cnt+1] = time+1
                    q.append((ni, nj, time+1, cnt+1))

    return -1


K = int(input())
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(bfs(0, 0))