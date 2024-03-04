N, M, i, j, K = map(int, input().split())
arr = []
# 최초 모든 면이 0
dice = {k: 0 for k in range(1, 7)}
for _ in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)

delta = ((0, 1), (0, -1), (-1, 0), (1, 0))
# 최초 윗면 인덱스
# idx = 1
# 윗면의 이동
# move = {1: (4, 3, 5, 2), 2: (4, 3, 1, 6), 3: (1, 6, 5, 2), 4: (6, 1, 5, 2), 5: (4, 3, 6, 1), 6: (4, 3, 1, 5)}
x = [3, 1, 4, 6]
y = [1, 5, 6, 2]

order = list(map(int, input().split()))
ci, cj = i, j
for d in order:
    di, dj = delta[d-1]
    ni, nj = ci+di, cj+dj
    if 0 <= ni < N and 0 <= nj < M:
        if d == 1:
            y[0], y[2] = x[2], x[0]
            x = x[1:]+[x[0]]
            if arr[ni][nj]:
                arr[ni][nj], dice[x[3]] = 0, arr[ni][nj]
            else:
                arr[ni][nj] = dice[x[3]]
            print(dice[x[1]])
        elif d == 2:
            y[0], y[2] = x[0], x[2]
            x = [x[-1]] + x[:-1]
            if arr[ni][nj]:
                arr[ni][nj], dice[x[3]] = 0, arr[ni][nj]
            else:
                arr[ni][nj] = dice[x[3]]
            print(dice[x[1]])
        elif d == 3:
            x[1], x[3] = y[1], y[3]
            y = y[1:] + [y[0]]
            if arr[ni][nj]:
                arr[ni][nj], dice[y[2]] = 0, arr[ni][nj]
            else:
                arr[ni][nj] = dice[y[2]]
            print(dice[y[0]])
        else:
            x[1], x[3] = y[3], y[1]
            y = [y[-1]]+y[:-1]
            if arr[ni][nj]:
                arr[ni][nj], dice[y[2]] = 0, arr[ni][nj]
            else:
                arr[ni][nj] = dice[y[2]]
            print(dice[y[0]])
        ci, cj = ni, nj