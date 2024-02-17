N = int(input())
arr = [[0] * 100 for _ in range(100)]
ans = 0

for tc in range(1, N+1):
    sx, sy = map(int, input().split())
    for i in range(sx, sx+10):
        for j in range(sy, sy+10):
            arr[i][j] = tc

for i in range(100):
    for j in range(100):
        # 아랫변
        if i+1 < 100:
            if arr[i+1][j] == 0 and arr[i][j]:
                ans += 1
            elif i == 99:
                ans += 1
        if i == 99 and arr[i][j]:
            ans += 1
        # 윗변
        if i-1 >= 0:
            if arr[i-1][j] == 0 and arr[i][j]:
                ans += 1
        if i == 0 and arr[i][j]:
            ans += 1
        # 좌변
        if j-1 >= 0:
            if arr[i][j-1] == 0 and arr[i][j]:
                ans += 1
        if j == 0 and arr[i][j]:
            ans += 1
        # 우변
        if j+1 < 100:
            if arr[i][j+1] == 0 and arr[i][j]:
                ans += 1
        if j == 99 and arr[i][j]:
            ans +=1

print(ans)