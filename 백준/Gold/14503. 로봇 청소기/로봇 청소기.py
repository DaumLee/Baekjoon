def check(ci, cj):
    for di, dj in delta:
        ni, nj = ci+di, cj+dj
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 0:
            return True
    return False


def solve(si, sj, d):
    global cnt

    ci, cj = si, sj
    while True:
        # 1번, 현재 자리 청소
        if board[ci][cj] == 0:
            board[ci][cj] = 2
            cnt += 1
        # 3번 : 청소
        if check(ci, cj):
            # 반시계 방향 회전
            d = (d-1) % 4
            # 4방향 탐색
            for i in range(4):
                ni, nj = ci+delta[d][0], cj+delta[d][1]
                # 갈 수 있으면 간 후 1번으로 회귀
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 0:
                    ci, cj = ni, nj
                    break
                # 못 가면 다시 90도 회전
                else:
                    d = (d-1) % 4
        # 2번
        else:
            ni, nj = ci-delta[d][0], cj-delta[d][1]
            # 2-1번 : 벽이 아니면 후진
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 1:
                ci = ni
                cj = nj
            # 2-2번 : 종료
            else:
                break


N, M = map(int, input().split())
si, sj, dir = map(int, input().split())
# 북 동 남 서
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
# 0 : 청소하지 않은 칸 / 1 : 벽 / 2 : 청소한 칸
board = [list(map(int, input().split())) for _ in range(N)]
# 청소한 칸 수
cnt = 0

solve(si, sj, dir)

print(cnt)