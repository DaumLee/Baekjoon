def check(ci, cj):

    for d in delta:
        ni, nj = ci+d[0], cj+d[1]
        # 내 위치에서 갈 수 있는 곳이 존재하면 종료하지 않음
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != -1 and not v[ni][nj]:
            return False
    # 내 위치에서 갈 수 있는 곳이 없으면 종료함
    return True


def go(idx):
    global ci, cj, d
    ni, nj = ci+delta[idx][0], cj+delta[idx][1]
    # 장애물이 아니고, 범위 내에서 방문한 적이 없는 곳으로 갈 수 있으면
    if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and board[ni][nj] != -1:
        v[ni][nj] = 1
        ci, cj = ni, nj
        return
    # 못가면 다음 방향으로 변경
    else:
        d = (d+1) % 4
        return


N, M = map(int, input().split())

board = [[0] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]

# 장애물 체크
t = int(input())
for i in range(t):
    ti, tj = map(int, input().split())
    board[ti][tj] = -1

ci, cj = map(int, input().split())
v[ci][cj] = 1
# 오른쪽(4), 위(1), 아래(2), 왼쪽(3)
delta = ((0, 1), (-1, 0), (1, 0), (0, -1))
# 방향 인덱스 진행 순서
lst = list(map(int, input().split()))
d = 0

while True:
    # 인덱스를 줌
    go(lst[d] % 4)

    # 종료조건 체크
    if check(ci, cj):
        break

print(ci, cj)