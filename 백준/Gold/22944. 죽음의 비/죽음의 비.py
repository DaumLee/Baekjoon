from collections import deque


def bfs(si, sj):
    q = deque([(si, sj, H, 0)])
    v = [[[0, 0] for j in range(N)] for i in range(N)]
    v[si][sj] = [1, H]
    while q:
        ci, cj, h, d = q.popleft()
        if board[ci][cj] == 'E':
            return v[ci][cj][0]-1
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and (not v[ni][nj][0] or v[ni][nj][1] < h+d-1):
                # 우산에서 내구도 초기화
                if board[ni][nj] == 'U':
                    v[ni][nj] = [v[ci][cj][0]+1, h+D-1]
                    q.append((ni, nj, h, D-1))
                # 내구도가 있으면 내구도 감소
                elif d > 0:
                    v[ni][nj] = [v[ci][cj][0]+1, h+d-1]
                    q.append((ni, nj, h, d-1))
                # 내구도가 없고 체력이 있으면 체력 감소
                elif h > 1 or (h > 0 and board[ni][nj] == 'E'):
                    v[ni][nj] = [v[ci][cj][0]+1, h+d-1]
                    q.append((ni, nj, h-1, d))
    return -1


N, H, D = map(int, input().split())
board = []
for i in range(N):
    lst = list(input())
    board.append(lst)
    for j in range(N):
        if lst[j] == 'S':
            si, sj = i, j

print(bfs(si, sj))