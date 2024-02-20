from collections import deque


def bfs(start):
    q = deque(start)
    v = [[0] * N for _ in range(N)]

    while q:
        d, ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            # 바이러스가 침범하지 않은 영역으로 전염, S초가 지나면 더 나아가지 않고 종료
            if 0 <= ni < N and 0 <= nj < N and not board[ni][nj] and v[ci][cj] < S:
                board[ni][nj] = d
                v[ni][nj] = v[ci][cj] + 1
                q.append((d, ni, nj))

    print(board[X-1][Y-1])


N, K = map(int, input().split())
board = []
virus = []
for i in range(N):
    lst = list(map(int, input().split()))
    board.append(lst)
    for j in range(N):
        if lst[j]:
            virus.append((lst[j], i, j))

# 바이러스 번호 순 정렬
virus.sort()
# S초, 목적 인덱스
S, X, Y = map(int, input().split())

bfs(virus)