from collections import deque
from itertools import combinations


def bfs(start, w):
    global ans

    q = deque(start)
    v = [[0] * M for _ in range(N)]

    while q:
        ci, cj = q.popleft()
        # 바이러스 전염
        v[ci][cj] = 1
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if (ni, nj) in w:
                continue
            # 기존 벽에 안막히면 진행
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and board[ni][nj] != 1:
                v[ni][nj] = 1
                q.append((ni, nj))

    # 벽 3개 제외
    sm = -3
    for line in v:
        sm += line.count(0)

    for line in board:
        sm -= line.count(1)

    ans = max(ans, sm)

N, M = map(int, input().split())
board = []
# 바이러스 위치(bfs 시작)
virus = []
# 빈칸의 위치
blank = []
for i in range(N):
    lst = list(map(int, input().split()))
    board.append(lst)
    for j in range(M):
        if lst[j] == 2:
            virus.append((i, j))
        elif lst[j] == 0:
            blank.append((i, j))

ans = 0

# 빈 칸 세 곳에 벽을 치자
for wall in combinations(blank, 3):
    bfs(virus, wall)

print(ans)