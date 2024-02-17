import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sm = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if j == 0:
            sm[i][j] = arr[i-1][j-1]
        else:
            sm[i][j] = sm[i][j-1] + arr[i-1][j-1]


for _ in range(M):
    ans = 0
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2+1):
        ans += sm[i][x2]-sm[i][x1-1]

    print(ans)