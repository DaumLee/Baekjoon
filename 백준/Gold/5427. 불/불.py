from collections import deque


def bfs(s):
    q = deque(s)
    v = [[0] * M for _ in range(N)]
    v[s[-1][0]][s[-1][1]] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj
            if (ni == -1 or ni == N or nj == -1 or nj == M) and board[ci][cj] == '@':
                return v[ci][cj]
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and board[ni][nj] != '#' and board[ni][nj] != '*' and board[ni][nj] != '@':
                board[ni][nj] = board[ci][cj]
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
    return 'IMPOSSIBLE'


T = int(input())
for tc in range(T):
    M, N = map(int, input().split())
    board = []
    start = []
    magma = []
    for i in range(N):
        lst = list(input())
        board.append(lst)
        for j in range(M):
            if lst[j] == '@':
                start.append((i, j))
            elif lst[j] == '*':
                magma.append((i, j))
    print(bfs(magma+start))