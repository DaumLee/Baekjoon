def move(d):
    global idx, ci, cj, flag

    di, dj = delta[idx]
    for k in range(d):
        ni, nj = ci+di, cj+dj
        if 0 <= ni < M and 0 <= nj < M:
            ci, cj = ni, nj
            board[ci][cj] = 1
        else:
            flag = 0
            break


def turn(dir):
    global idx

    # dir이 1이면 왼쪽으로 회전
    if dir:
        idx = (idx-1) % 4
    # dir이 0이면 오른쪽으로 회전
    else:
        idx = (idx+1) % 4


M, n = map(int, input().split())
board = [[0] * M for _ in range(M)]
idx = 0
# 이동 방향
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
ci = cj = 0
board[ci][cj] = 1
# 조건 분기
flag = 1
# 명령어 처리
for i in range(n):
    if flag:
        o, d = input().split()
        if o == 'MOVE':
            move(int(d))
        else:
            turn(int(d))

if flag:
    print(cj, ci)
else:
    print(-1)