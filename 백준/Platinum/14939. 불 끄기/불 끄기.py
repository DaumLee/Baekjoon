def solve(on):
    board = [line[:] for line in arr]
    cnt = len(on)
    for j in range(10):
        if j in on:
            for di, dj in delta:
                ni, nj = di, j+dj
                if 0 <= ni < 10 and 0 <= nj < 10:
                    board[ni][nj] ^= 1

    for i in range(1, 10):
        for j in range(10):
            if board[i-1][j]:
                for di, dj in delta:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        board[ni][nj] ^= 1
                cnt += 1

    # 켜져있는 전구가 있다면 불가능
    if sum(board[9]):
        return -1
    return cnt


def switch(n, lst):
    global ans

    if n == 10:
        ret = solve(lst)
        if ret != -1:
            if ans == -1:
                ans = ret
            else:
                ans = min(ans, ret)
        return

    switch(n+1, lst+[n])
    switch(n+1, lst)


arr = []
for i in range(10):
    lst = list(input())
    for j in range(10):
        if lst[j] == '#':
            lst[j] = 0
        else:
            lst[j] = 1
    arr.append(lst)

ans = -1
delta = ((0, 0), (-1, 0), (1, 0), (0, 1), (0, -1))
switch(0, [])

print(ans)