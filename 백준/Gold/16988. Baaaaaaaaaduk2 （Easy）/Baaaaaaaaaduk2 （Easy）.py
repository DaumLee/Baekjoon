from collections import deque


def bfs(s, lst, v):
    global ans
    q = deque([s])
    flag = 1
    # 지금 칸 방문
    v[s[0]][s[1]] = 1
    # 시작 칸은 적 돌: 1개부터 시작
    cnt = 1
    # 아군 돌 2개 착수
    for wi, wj in lst:
        v[wi][wj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj
            # 붙어있는 돌로 이동 가능하면
            if 0 <= ni < N+2 and 0 <= nj < M+2 and not v[ni][nj] and board[ni][nj] != 1:
                if board[ni][nj] == 2:
                    v[ni][nj] = 1
                    cnt += 1
                    q.append((ni, nj))
                elif board[ni][nj] == 0:
                    flag = 0
    return cnt, flag


def solve(n, si, sj, new):
    global ans
    # 혹시 끝에 도착하면 종료
    if n == 1 and si == N and sj == M:
        return
    # 둘 곳 두 군데 찾았으면
    if n == 2:
        # 가장자리는 아군 돌로 가정
        v = [[1]*(M+2)]+[[1]+[0]*M+[1] for _ in range(N)]+[[1]*(M+2)]
        sm = 0
        # 모든 적 집합에서 bfs
        for e in enemy:
            if v[e[0]][e[1]]:
                continue
            # 함수 ㄱ
            c, f = bfs(e, new, v)
            if f:
                sm += c
        # if ans < sm:
        #     print(new)
        ans = max(ans, sm)
        return

    for i in range(si, N+1):
        for j in range(M+1):
            # 이전 돌과는 조합이 이미 이루어짐
            if i == si and j < sj:
                continue
            # 둘 수 있는 칸이면 선택해봄
            if board[i][j] == 0 and (i, j) not in new:
                solve(n+1, i, j, new+[(i, j)])


N, M = map(int, input().split())
board = [[1]*(M+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(M+2)]
enemy = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] == 2:
            enemy.append((i, j))

ans = 0
solve(0, 1, 1, [])
print(ans)