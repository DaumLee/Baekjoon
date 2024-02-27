from collections import deque


def bfs(si, sj):
    q = deque([(si, sj)])
    v = [[0] * 501 for _ in range(501)]
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            # 범위 내에서 방문하지 않았거나, 현재 깎인 체력이 더 적고 죽음의 구역이 아니면 진행
            if 0 <= ni < 501 and 0 <= nj < 501 and (not v[ni][nj] or (board[ni][nj] and v[ni][nj] > v[ci][cj]+1) or (not board[ni][nj] and v[ni][nj] > v[ci][cj])) and board[ni][nj] != 2:
                if board[ni][nj]:
                    v[ni][nj] = v[ci][cj] + 1
                else:
                    v[ni][nj] = v[ci][cj]
                q.append((ni, nj))

    if v[500][500]:
        print(v[500][500]-1)
    else:
        print(-1)


board = [[0] * 501 for _ in range(501)]
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(y1, y2), max(y1, y2)+1):
        for j in range(min(x1, x2), max(x1, x2)+1):
            board[i][j] = 1

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(y1, y2), max(y1, y2)+1):
        for j in range(min(x1, x2), max(x1, x2)+1):
            board[i][j] = 2

bfs(0, 0)