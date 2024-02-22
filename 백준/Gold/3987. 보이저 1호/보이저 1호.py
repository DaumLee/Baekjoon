def turn(ci, cj, idx):

    if graph[ci][cj] == '/':
        idx = rf1[idx]
    elif graph[ci][cj] == '\\':
        idx = rf2[idx]

    return idx


def solve(si, sj, i):
    global mx, dr

    idx = i
    ci, cj = si, sj
    time = 0

    while True:
        # 타임아웃이면 Voyager
        if time > N * M * 2:
            mx = 'Voyager'
            dr = i
            return

        # 행성에서 방향 전환 확인
        idx = turn(ci, cj, idx)
        ni, nj = ci+delta[idx][0], cj+delta[idx][1]
        # 갈 수 있으면 한칸 나아감
        if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] != 'C':
            ci, cj = ni, nj
            time += 1
        # 갈 수 없으면 종료하고 최댓값 갱신
        else:
            if mx < time:
                mx = time+1
                dr = i
            return


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
# 시작점
si, sj = map(int, input().split())
# 위, 오른쪽, 아래, 왼쪽
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
# 최대 시간
mx = 0
# 정답 방향
dr = 0
dct = {0: 'U', 1: 'R', 2: 'D', 3: 'L'}

# / 반사
rf1 = {0: 1, 1: 0, 2: 3, 3: 2}
# \ 반사
rf2 = {0: 3, 1: 2, 2: 1, 3: 0}

# 4 방향 시그널 모두 시도
for i in range(4):
    if type(mx) != str:
        # 좌표를 (0, 0) ~ (N-1, M-1)로 맞춰줌
        solve(si-1, sj-1, i)

# 방향은 문자로 출력
print(dct[dr])
print(mx)