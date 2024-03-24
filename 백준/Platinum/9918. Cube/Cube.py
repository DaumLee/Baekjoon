def rotate(d, ni, nj, f):
    if d == 0:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif d == 1:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif d == 2:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    else:
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
    if f:
        dice[5] = arr[ni][nj]

def roll(ci, cj):
    for d in range(4):
        di, dj = delta[d]
        ni, nj = ci+di, cj+dj
        # 1이 있는 칸으로(주사위를 만들 수 있는 칸으로) 이동
        if 0 <= ni < 6 and 0 <= nj < 6 and arr[ni][nj] and not v[ni][nj]:
            v[ni][nj] = 1
            # d 방향으로 진행하고
            rotate(d, ni, nj, 1)
            roll(ni, nj)
            # 원상 복구
            rotate(turn[d], ni, nj, 0)

def find(dice):
    for i in range(6):
        # 1을 찾으면
        if dice[i] == 1:
            # 마주보는 면 출력
            print(dice[ans[i]])
            return

delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
turn = {0: 1, 1: 0, 2: 3, 3: 2}
arr = [list(map(int, input().split())) for _ in range(6)]
v = [[0] * 6 for _ in range(6)]
# 서로 마주보는 면 인덱스
ans = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}
dice = [0] * 6
flag = 0
for i in range(6):
    # 이미 주사위를 굴렸으면
    if flag:
        break
    for j in range(6):
        if arr[i][j]:
            v[i][j] = 1
            dice[5] = arr[i][j]
            roll(i, j)
            flag = 1
            break
if 0 in dice:
    print(0)
else:
    find(dice)