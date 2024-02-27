from collections import deque


def air(si, sj):
    q = deque([(si, sj)])
    v = [[0] * M for _ in range(N)]

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and (board[ni][nj] == 0 or board[ni][nj] == 2):
                v[ni][nj] = 1
                board[ni][nj] = 2
                q.append((ni, nj))


def bfs(s):
    global cnt, last

    q = deque(s)
    chz = []

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            # 외부공기랑 만난 적 있으면
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 2:
                chz.append((ci, cj))
                break

    last = len(chz)
    cnt -= last
    for ci, cj in chz:
        # 지운 치즈는 외부 공기로 변함
        board[ci][cj] = 2


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 전체 치즈 개수
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cnt += 1

air(0, 0)
time = 0
last = 0
while True:
    time += 1
    start = []
    for i in range(N):
        for j in range(M):
            # 치즈의 사방 탐색
            if board[i][j] == 1:
                start.append((i, j))
    bfs(start)
    air(0, 0)
    if cnt <= 0:
        break

print(time)
print(last)