def move(num, ci, cj, cd):
    for idx in range(len(board[ci][cj])):
        if board[ci][cj][idx] == num:
            start = idx
            break
    di, dj = delta[cd]
    ni, nj = ci+di, cj+dj
    if arr[ni][nj] == 0:
        for n in board[ci][cj][start:]:
            d = p[n][2]
            p[n] = (ni, nj, d)
        board[ni][nj] += board[ci][cj][start:]
        if len(board[ni][nj]) >= 4:
            return True
        board[ci][cj] = board[ci][cj][:start]
    elif arr[ni][nj] == 1:
        for n in board[ci][cj][start:]:
            d = p[n][2]
            p[n] = (ni, nj, d)
        board[ni][nj] += board[ci][cj][start:][::-1]
        if len(board[ni][nj]) >= 4:
            return True
        board[ci][cj] = board[ci][cj][:start]
    return False


def play():
    for i in range(1, num):
        ci, cj, cd = p[i]
        di, dj = delta[cd]
        ni, nj = ci+di, cj+dj
        if arr[ni][nj] != 2:
            if move(i, ci, cj, cd):
                return True
        else:
            cd ^= 1
            if move(i, ci, cj, cd):
                return True
            p[i] = (p[i][0], p[i][1], cd)
    return False


N, K = map(int, input().split())
arr = [[2]*(N+2)] + [[2]+list(map(int, input().split()))+[2] for _ in range(N)] + [[2]*(N+2)]
board = [[list() for _ in range(N+2)] for _ in range(N+2)]
delta = ((0, 1), (0, -1), (-1, 0), (1, 0))
p = dict()
num = 1
for _ in range(K):
    si, sj, d = map(int, input().split())
    board[si][sj].append(num)
    p[num] = (si, sj, d-1)
    num += 1
time = 0
while time <= 1000:
    time += 1
    if play():
        break
if time == 1001:
    print(-1)
else:
    print(time)