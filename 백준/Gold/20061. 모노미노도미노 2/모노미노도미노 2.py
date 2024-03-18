def on_blue(t, x):
    global ans, blue
    if t == 1:
        bj = 0
        for j in range(6):
            # 해당 칸이 비었으면
            if not blue[x][j]:
                bj = j
            else:
                break
        blue[x][bj] = 1
    elif t == 2:
        bj = 0
        for j in range(5):
            # 해당 칸이 비었으면
            if not blue[x][j+1] and not blue[x][j]:
                bj = j
            else:
                break
        blue[x][bj] = blue[x][bj+1] = 1
    else:
        bj = 0
        for j in range(6):
            # 해당 칸이 비었으면
            if not blue[x+1][j] and not blue[x][j]:
                bj = j
            else:
                break
        blue[x+1][bj] = blue[x][bj] = 1
    # 점수 계산을 위해 회전
    blue = list(map(list, zip(*blue[::-1])))
    # 점수 획득 줄
    score_line = []
    for i in range(2, 6):
        if sum(blue[i]) == 4:
            score_line.append(i)
            ans += 1
            for j in range(4):
                blue[i][j] = 0
    # 점수 먹고 줄 내리기
    for k in score_line:
        for i in range(k-1, -1, -1):
            for j in range(4):
                blue[i][j], blue[i+1][j] = 0, blue[i][j]
    # 연한 칸 확인
    cnt = 0
    for i in range(2):
        # 연한 칸에 있으면 +1
        if sum(blue[i]) >= 1:
            cnt += 1
    # 연한 칸 처리
    if cnt >= 1:
        # 아래는 지우고
        for i in range(5, 5 - cnt, -1):
            for j in range(4):
                blue[i][j] = 0
        # 위는 내리고
        for i in range(5 - cnt, -1, -1):
            for j in range(4):
                blue[i][j], blue[i+cnt][j] = 0, blue[i][j]
    # 원상 복구
    blue = list(map(list, zip(*blue)))[::-1]


def on_green(t, y):
    global ans, green
    if t == 1:
        gi = 0
        for i in range(6):
            if not green[i][y]:
                gi = i
            else:
                break
        green[gi][y] = 1
    elif t == 2:
        gi = 0
        for i in range(6):
            if not green[i][y] and not green[i][y+1]:
                gi = i
            else:
                break
        green[gi][y] = green[gi][y+1] = 1
    else:
        gi = 0
        for i in range(5):
            if not green[i][y] and not green[i+1][y]:
                gi = i
            else:
                break
        green[gi][y] = green[gi+1][y] = 1

    # 점수 획득 줄
    score_line = []
    # 점수 계산
    for i in range(2, 6):
        if sum(green[i]) == 4:
            score_line.append(i)
            ans += 1
            for j in range(4):
                green[i][j] = 0
    # 점수 먹고 줄 내리기
    for k in score_line:
        for i in range(k-1, -1, -1):
            for j in range(4):
                green[i][j], green[i+1][j] = 0, green[i][j]
    # 연한 칸 확인
    cnt = 0
    for i in range(2):
        # 연한 칸에 있으면 +1
        if sum(green[i]) >= 1:
            cnt += 1
    # 연한 칸 처리
    if cnt >= 1:
        # 아래는 지우고
        for i in range(5, 5-cnt, -1):
            for j in range(4):
                green[i][j] = 0
        # 위는 내리고
        for i in range(5-cnt, -1, -1):
            for j in range(4):
                green[i][j], green[i+cnt][j] = 0, green[i][j]


N = int(input())

blue = [[0] * 6 for _ in range(4)]
green =[[0] * 4 for _ in range(6)]

ans = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    on_blue(t, x)
    on_green(t, y)
print(ans)
blocks = 0
for i in range(4):
    for j in range(6):
        if blue[i][j]:
            blocks += 1
for i in range(6):
    for j in range(4):
        if green[i][j]:
            blocks += 1
print(blocks)