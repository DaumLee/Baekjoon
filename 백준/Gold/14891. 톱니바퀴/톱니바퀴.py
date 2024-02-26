# 회전하는 톱니바퀴 체크
def check(c):
    for d in (-1, 1):
        n = c+d
        if 0 <= n < 4 and not v[n]:
            # c가 왼쪽 톱니바퀴면
            if c < n and lst[c][(idx[c][0]+2)%8] != lst[n][(idx[n][1]-1)%8]:
                turn[n] = True
                v[n] = 1
                check(n)
            # c가 오른쪽 톱니바퀴면
            elif c > n and lst[c][(idx[c][1]-1)%8] != lst[n][(idx[n][0]+2)%8]:
                turn[n] = True
                v[n] = 1
                check(n)
    return turn


def roll(n, d):
    check(n)
    # 반시계 방향 회전
    if d == -1:
        for c in range(4):
            # 회전하는 톱니바퀴고 다른 위치로 회전
            if turn[c] and abs(n-c) % 2:
                idx[c][0] = (idx[c][0]-1) % 8
                idx[c][1] = (idx[c][1]-1) % 8
            # 회전하는 톱니바퀴고 같은 위치로 회전
            elif turn[c]:
                idx[c][0] = (idx[c][0]+1) % 8
                idx[c][1] = (idx[c][1]+1) % 8
    else:
        for c in range(4):
            # 회전하는 톱니바퀴고 다른 위치로 회전
            if turn[c] and abs(n-c) % 2:
                idx[c][0] = (idx[c][0]+1) % 8
                idx[c][1] = (idx[c][1]+1) % 8
            # 회전하는 톱니바퀴고 같은 위치로 회전
            elif turn[c]:
                idx[c][0] = (idx[c][0]-1) % 8
                idx[c][1] = (idx[c][1]-1) % 8


lst = [input() for _ in range(4)]
K = int(input())
# 각각 12시의 인덱스, 10시반의 인덱스
idx = [[0, 7] for _ in range(4)]
for _ in range(K):
    n, d = map(int, input().split())
    v = [0] * 4
    v[n-1] = 1
    turn = [False] * 4
    turn[n-1] = True
    roll(n-1, d)

sm = 0

for i in range(4):
    if lst[i][idx[i][0]] == '1':
        sm += 2**i

print(sm)