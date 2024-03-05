from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj):
    q = deque([(si, sj, 0)])
    v = [[[-1 for j in range(M)] for i in range(N)] for k in range(K+1)]
    v[0][si][sj] = 1

    while q:
        ci, cj, cnt = q.popleft()
        # 목적지 도착
        if ci == N-1 and cj == M-1:
            return v[cnt][ci][cj]
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                # 벽 부수기
                if cnt < K and arr[ni][nj] == '1' and (v[cnt+1][ni][nj] == -1 or v[cnt+1][ni][nj] > v[cnt][ci][cj]+1):
                    v[cnt+1][ni][nj] = v[cnt][ci][cj]+1
                    q.append((ni, nj, cnt+1))
                # 빈칸 최단 거리 이동
                if arr[ni][nj] == '0' and (v[cnt][ni][nj] == -1 or v[cnt][ni][nj] > v[cnt][ci][cj]+1):
                    v[cnt][ni][nj] = v[cnt][ci][cj]+1
                    q.append((ni, nj, cnt))

    return -1


N, M, K = map(int, input().split())
arr = [input() for _ in range(N)]
print(bfs(0, 0))