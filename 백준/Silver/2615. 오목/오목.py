def check(arr):
    for i in range(19):
        for j in range(19):
            item = arr[i][j]
            # 돌이 없으면 탐색하지 않음
            if item == 0:
                continue
            for dy, dx in d:
                cnt = 0
                for k in range(-1, 6):
                    ny = i + k * dy
                    nx = j + k * dx
                    if 0 <= ny < 19 and 0 <= nx < 19:
                        # 이전 돌이 현재 돌과 같으면 탐색하지 않음
                        if k == -1 and arr[ny][nx] == item:
                            break
                        elif arr[ny][nx] == item:
                            cnt += 1
                        # 탐색 범위에서 나랑 다른 돌을 만나면 break
                        elif k != -1 and arr[ny][nx] != item:
                            break
                if cnt == 5:
                    return [item, i+1, j+1]


arr = [list(map(int, input().split())) for _ in range(19)]
d = [(1, 0), (0, 1), (1, 1), (-1, 1)]

ans = check(arr)

if ans:
    print(ans[0])
    print(ans[1], ans[2])
else:
    print(0)