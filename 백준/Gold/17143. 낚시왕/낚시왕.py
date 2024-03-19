def catch(j):
    for i in range(1, N+1):
        if arr[i][j]:
            # 잡았다
            ret = arr[i][j][0]
            # 맵에서 제거
            arr[i][j] = []
            return ret

def move():
    board = [[list()] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j]:
                # print(arr[i][j])
                size, cs, cd = arr[i][j]
                ci, cj = i, j
                di, dj = delta[cd]
                for k in range(cs):
                    ni, nj = ci+di, cj+dj
                    if 1 <= ni <= N and 1 <= nj <= M:
                        ci, cj = ni, nj
                    else:
                        cd = turn[cd]
                        di, dj = delta[cd]
                        ci, cj = ci+di, cj+dj
                if board[ci][cj]:
                    if board[ci][cj][0] < size:
                        board[ci][cj] = (size, cs, cd)
                else:
                    board[ci][cj] = (size, cs, cd)
    return board

N, M, K = map(int, input().split())
arr = [[list()] * (M+1) for _ in range(N+1)]
delta = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}
turn = {1: 2, 2: 1, 3: 4, 4: 3}
for _ in range(K):
    si, sj, s, d, size = map(int, input().split())
    arr[si][sj] = (size, s, d)

lst = []
for i in range(1, M+1):
    c = catch(i)
    if c:
        lst.append(c)
    arr = move()
print(sum(lst))