def check(arr):
    global ans
    remove = []
    for i in range(2, 6):
        if sum(arr[i]) == 4:
            remove.append(i)
            ans += 1
            for j in range(4):
                arr[i][j] = 0
    for k in remove:
        for i in range(k-1, -1, -1):
            for j in range(4):
                if arr[i][j]: arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
    cnt = 0
    for i in range(2):
        if sum(arr[i]):
            cnt += 1
    for i in range(5, 5-cnt, -1):
        for j in range(4):
            arr[i][j] = 0
    for _ in range(cnt):
        for i in range(4, -1, -1):
            for j in range(4):
                if arr[i][j]: arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
    return arr


def play(arr, t, y):
    if t == 1:
        blocks = [(0, y)]
    elif t == 2:
        blocks = [(0, y), (0, y+1)]
    else:
        blocks = [(1, y), (0, y)]
    flag = 0
    for i in range(6):
        for bi, bj in blocks:
            # t==3일 때 블록이 세워질 수 없으면 stop
            if i+bi > 5:
                ei = i-1
                flag = 1
                break
            if arr[i+bi][bj]:
                ei = i-1
                flag = 1
                break
        if flag: break
    else:
        ei = 5
    if t == 1:
        x, y = blocks[0]
        arr[ei][y] = 1
    elif t == 2:
        for x, y in blocks:
            arr[ei][y] = 1
    else:
        for x, y in blocks:
            arr[ei][y] = 1
            ei += 1
    return arr


K = int(input())
red = [[0] * 4 for _ in range(6)]
yellow = [[0] * 4 for _ in range(6)]
ans = 0
for _ in range(K):
    t, x, y = map(int, input().split())
    if t == 1:
        red = play(red, t, 3-x)
        yellow = play(yellow, t, y)
    elif t == 2:
        red = play(red, t^1, 3-x)
        yellow = play(yellow, t, y)
    else:
        red = play(red, t^1, 2-x)
        yellow = play(yellow, t, y)
    red = check(red)
    yellow = check(yellow)
print(ans)
cnt = 0
for i in range(6):
    for j in range(4):
        if red[i][j]: cnt += 1
        if yellow[i][j]: cnt += 1
print(cnt)