def turn(ci, cj, idx):
    if graph[ci][cj] == '/' and idx == 2:
        idx = 3
    elif graph[ci][cj] == '/' and idx == 1:
        idx = 0
    elif graph[ci][cj] == '/' and idx == 0:
        idx = 1
    elif graph[ci][cj] == '/' and idx == 3:
        idx = 2
    elif graph[ci][cj] == '\\' and idx == 2:
        idx = 1
    elif graph[ci][cj] == '\\' and idx == 3:
        idx = 0
    elif graph[ci][cj] == '\\' and idx == 1:
        idx = 2
    elif graph[ci][cj] == '\\' and idx == 0:
        idx = 3
    return ci, cj, idx


def solve(si, sj, i):
    global mx, dir

    idx = i
    ci, cj = si, sj
    time = 0
    while True:
        if time > N*M * 2:
            mx = 'Voyager'
            dir = i
            return
        # 행성에서 방향 전환
        ci, cj, idx = turn(ci, cj, idx)
        ni, nj = ci+delta[idx][0], cj+delta[idx][1]
        if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] != 'C':
            ci, cj = ni, nj
            time += 1
        else:
            if mx < time:
                mx = time+1
                dir = i
            return


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

si, sj = map(int, input().split())
# 위, 오른쪽, 아래, 왼쪽
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
# 최대 시간
mx = 0
# 정답 방향
dir = 0

for i in range(4):
    if type(mx) != str:
        solve(si-1, sj-1, i)

if dir == 0:
    dir = 'U'
elif dir == 1:
    dir = 'R'
elif dir == 2:
    dir = 'D'
else:
    dir = 'L'

print(dir)
print(mx)