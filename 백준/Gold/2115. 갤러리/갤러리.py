N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
v = [[[0] * M for _ in range(N)] for _ in range(4)]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            if i < N-1 and arr[i+1][j] == 'X':
                if j > 0:
                    if arr[i][j-1] == '.' and arr[i+1][j-1] == '.' and not v[0][i][j-1] and not v[0][i+1][j-1]:
                        cnt += 1
                        v[0][i][j-1] = v[0][i+1][j-1] = 1
                if j < M-1:
                    if arr[i][j+1] == '.' and arr[i+1][j+1] == '.' and not v[1][i][j+1] and not v[1][i+1][j+1]:
                        cnt += 1
                        v[1][i][j+1] = v[1][i+1][j+1] = 1
            if j < M-1 and arr[i][j+1] == 'X':
                if i > 0:
                    if arr[i-1][j] == '.' and arr[i-1][j+1] == '.' and not v[2][i-1][j] and not v[2][i-1][j+1]:
                        cnt += 1
                        v[2][i-1][j] = v[2][i-1][j+1] = 1
                if i < N-1:
                    if arr[i+1][j] == '.' and arr[i+1][j+1] == '.' and not v[3][i+1][j] and not v[3][i+1][j+1]:
                        cnt += 1
                        v[3][i+1][j] = v[3][i+1][j+1] = 1
print(cnt)