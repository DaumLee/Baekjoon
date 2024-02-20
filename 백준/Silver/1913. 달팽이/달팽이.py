def solve(ci, cj):
    global d, idx

    while True:
        # 위로 갈 때
        if d == 0:
            # 중앙과 idx만큼 차이 나면 방향 전환
            if abs(ci - N//2) == idx:
                d += 1
        # 오른쪽으로 갈 때
        elif d == 1:
            # 중앙과 idx만큼 차이 나면 방향 전환
            if abs(cj - N//2) == idx:
                d += 1
        # 아래로 갈 때
        elif d == 2:
            # 중앙과 idx만큼 차이 나면 방향 전환
            if abs(ci - N//2) == idx:
                d += 1
        # 왼쪽으로 갈 때
        else:
            # 중앙과 idx만큼 차이 나면 방향 전환
            if abs(cj - N//2) == idx:
                d = 0
                idx += 1
                
        di, dj = delta[d]
        ni, nj = ci+di, cj+dj
        board[ni][nj] = board[ci][cj] + 1
        if board[ni][nj] == N**2:
            return
        ci, cj = ni, nj


N = int(input())
K = int(input())
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0
# idx만큼 떨어짐
idx = 1
board = [[0]*N for _ in range(N)]
board[N//2][N//2] = 1
solve(N//2, N//2)
for i in range(N):
    print(*board[i])
    for j in range(N):
        if board[i][j] == K:
            ans = (i+1, j+1)

print(*ans)