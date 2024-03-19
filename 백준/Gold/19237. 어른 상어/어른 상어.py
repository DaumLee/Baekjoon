from collections import defaultdict

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dirs = list(map(int, input().split()))
shark_d = defaultdict(int)
for i in range(M):
    shark_d[i+1] = dirs[i]
shark_prop = defaultdict(dict)
delta = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
for i in range(1, M+1):
    for j in range(1, 5):
        lst = tuple(map(int, input().split()))
        shark_prop[i][j] = lst

time = 0
smell = [[0 for j in range(N)] for i in range(N)]
remain = [i for i in range(1, M+1)]
while time < 1000:
    board = [[0] * N for _ in range(N)]
    # 냄새 확산
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                smell[i][j] = [arr[i][j], K]
    # 이동
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                # 현재 상어의 방향
                cd = shark_d[arr[i][j]]
                # 현재 상어의 방향에 따른 우선 순위
                prop = shark_prop[arr[i][j]][cd]
                # 이동 후보
                cand = []
                # 냄새가 없는 칸을 찾았는지
                flag = 0
                # 우선 순위로 순회하면서
                for sd in prop:
                    # 냄새가 없는 칸을 이미 찾았으면 종료
                    if flag:
                        break
                    # 방향을 체크
                    di, dj = delta[sd]
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt = 0
                        # 나랑 다른 냄새가 마킹되어 있으면
                        if smell[ni][nj] and arr[i][j] != smell[ni][nj][0]:
                            continue
                        # 내 냄새가 마킹되어 있으면 후보
                        if smell[ni][nj]:
                            cand.append((ni, nj, sd))
                        else:
                            cand = (ni, nj, sd)
                            flag = 1
                            break
                # 냄새가 없는 칸으로 진행
                if flag:
                    ai, aj, ad = cand
                    if not board[ai][aj] or board[ai][aj] > arr[i][j]:
                        if board[ai][aj]:
                            remain.remove(board[ai][aj])
                        board[ai][aj] = arr[i][j]
                    else:
                        remain.remove(arr[i][j])
                    # 방향 변경
                    shark_d[arr[i][j]] = ad
                # 모두 냄새가 있는 칸이라면
                elif cand:
                    # 제일 먼저 찾은 후보로 진행
                    ai, aj, ad = cand[0]
                    if not board[ai][aj] or board[ai][aj] > arr[i][j]:
                        if board[ai][aj]:
                            remain.remove(board[ai][aj])
                        board[ai][aj] = arr[i][j]
                    else:
                        remain.remove(arr[i][j])
                    # 방향 변경
                    shark_d[arr[i][j]] = ad
    # 냄새 유효시간 감소
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = 0
    time += 1
    arr = board
    if len(remain) == 1:
        print(time)
        break
else:
    print(-1)