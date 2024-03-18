def move(si, sj, flst, board, v):
    for num in range(1, 17):
        flag = 0
        # 이미 먹힌 물고기는 제외
        if num in flst:
            continue
        for i in range(4):
            if flag:
                break
            for j in range(4):
                if flag:
                    break
                if board[i][j] == num:
                    d = v[i][j]
                    cnt = 0
                    while cnt < 8:
                        di, dj = delta[d]
                        ni, nj = i+di, j+dj
                        if 0 <= ni < 4 and 0 <= nj < 4 and not (ni == si and nj == sj):
                            if board[ni][nj] and board[ni][nj] not in flst:
                                board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                                v[i][j], v[ni][nj] = v[ni][nj], d
                            else:
                                board[i][j], board[ni][nj] = 0, board[i][j]
                                v[i][j], v[ni][nj] = -1, d
                            flag = 1
                            break
                        else:
                            cnt += 1
                            d = (d+1)%8
    return board, v


# 상어의 위치, 먹이
def solve(si, sj, sd, flst, arr, dirs):
    global ans
    # if ans < sum(flst):
    #     print(si, sj, sd, flst)
    ans = max(ans, sum(flst))
    # 새 보드
    board = [lst[:] for lst in arr]
    v = [lst[:] for lst in dirs]
    board[si][sj] = 0
    board, v = move(si, sj, flst, board, v)
    for k in range(1, 4):
        ni, nj = si+delta[sd][0]*k, sj+delta[sd][1]*k
        if 0 <= ni < 4 and 0 <= nj < 4 and board[ni][nj]:
            solve(ni, nj, v[ni][nj], flst+[board[ni][nj]], board, v)


arr = []
dirs = []
for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    arr.append([a1, a2, a3, a4])
    dirs.append([b1-1, b2-1, b3-1, b4-1])
# 8방 이동 정보
delta = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
ans = 0
solve(0, 0, dirs[0][0], [arr[0][0]], arr, dirs)
print(ans)