def sorting1(arr):
    # 왼쪽 끝 점
    l_limit = 1
    # 오른쪽 끝 점
    r_limit = 2
    # 위에 올림
    arr[0][0], arr[1][1] = 0, arr[0][0]
    # 현재 높이
    height = 1
    # 정리 실행
    while True:
        if r_limit+height > N-1:
            break
        on = []
        for i in range(height, -1, -1):
            on.append(arr[i][l_limit:r_limit])
            for j in range(l_limit, r_limit):
                arr[i][j] = 0
        on = list(map(list, zip(*on[::-1])))
        nxt = []
        for idx in range(len(on)-1, -1, -1):
            nxt.append(on[idx])
        for i in range(len(on), 0, -1):
            for j in range(r_limit, r_limit+len(on[0])):
                arr[i][j] = nxt[i-1][j-r_limit]
                height = max(height, i)
        l_limit = r_limit
        r_limit = r_limit+len(on[0])


def sorting2(lst):
    tmp = []
    up = lst[:N//2]
    down = lst[N//2:]
    tmp.append(up[::-1])
    tmp.append(down)
    tmp2 = []
    first = tmp[1][:N//4][::-1]
    second = tmp[0][:N//4][::-1]
    third = tmp[0][N//4:]
    fourth = tmp[1][N//4:]
    tmp2.append(fourth)
    tmp2.append(third)
    tmp2.append(second)
    tmp2.append(first)
    return tmp2


def divide(arr):
    new_arr = [lst[:] for lst in arr]
    for i in range(len(new_arr)):
        for j in range(len(new_arr[0])):
            # 아래 인접 확인
            if i <= len(new_arr) - 2:
                if arr[i][j] and arr[i + 1][j]:
                    d = abs(arr[i][j] - arr[i + 1][j]) // 5
                    if d > 0:
                        if arr[i][j] > arr[i + 1][j]:
                            new_arr[i][j] -= d
                            new_arr[i + 1][j] += d
                        else:
                            new_arr[i][j] += d
                            new_arr[i + 1][j] -= d
            if j <= len(new_arr[0]) - 2:
                if arr[i][j] and arr[i][j + 1]:
                    d = abs(arr[i][j] - arr[i][j + 1]) // 5
                    if d > 0:
                        if arr[i][j] > arr[i][j + 1]:
                            new_arr[i][j] -= d
                            new_arr[i][j + 1] += d
                        else:
                            new_arr[i][j] += d
                            new_arr[i][j + 1] -= d
    return new_arr


N, K = map(int, input().split())
lst = list(map(int, input().split()))
time = 0
while True:
    time += 1
    # 최소 어항에 물고기 추가
    mn = 10001
    add = []
    for i in range(N):
        if lst[i] < mn:
            mn = lst[i]
            add = [i]
        elif lst[i] == mn:
            add.append(i)
    for i in add:
        lst[i] += 1
    arr = [[0] * N for _ in range(N//2)]
    for i in range(N):
        arr[0][i] = lst[i]
    sorting1(arr)

    # 물고기 수 조절
    new_arr = divide(arr)
    lst = []
    for j in range(N):
        for i in range(N//2):
            if new_arr[i][j]:
                lst.append(new_arr[i][j])
    # 두 번째 정리
    arr = sorting2(lst)
    # 물고기 수 조절
    new_arr = divide(arr)
    lst = []
    for j in range(len(new_arr[0])):
        for i in range(len(new_arr)):
            if new_arr[i][j]:
                lst.append(new_arr[i][j])
    # 종료 조건
    if max(lst) - min(lst) <= K:
        print(time)
        break