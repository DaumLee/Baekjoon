N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if 0 <= j-1 and 0 <= i-1:
            arr[i][j] += max(arr[i][j - 1], arr[i - 1][j], arr[i - 1][j - 1])
        elif 0 <= j-1:
            arr[i][j] += arr[i][j - 1]
        elif 0 <= i-1:
            arr[i][j] += arr[i-1][j]

print(arr[N-1][M-1])