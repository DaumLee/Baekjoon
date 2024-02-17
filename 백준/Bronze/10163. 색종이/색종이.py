N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
ans = [0] * N

for tc in range(1, N+1):
    # sx가 가장 왼쪽 / sy가 가장 위
    sx, sy, dx, dy = map(int, input().split())
    for i in range(dx):
        for j in range(dy):
            arr[sx+i][sy+j] = tc

for i in range(1001):
    for j in range(1001):
        if arr[i][j] != 0:
            num = arr[i][j]-1
            ans[num] += 1

for i in range(len(ans)):
    print(ans[i])