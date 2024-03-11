
def move(ci, cj, d):
    global ans
    _10 = arr[ci][cj] // 10
    _7 = (arr[ci][cj] * 7) // 100
    _5 = arr[ci][cj] // 20
    _2 = arr[ci][cj] // 50
    _1 = arr[ci][cj] // 100
    if d == 0:
        if 0 <= ci-1:
            arr[ci-1][cj] += _7
            arr[ci-1][cj+1] += _1
        else:
            ans += _7 + _1
        if 0 <= ci-1 and 0 <= cj-1: arr[ci-1][cj-1] += _10
        else:   ans += _10
        if 0 <= ci-2:   arr[ci-2][cj] += _2
        else:   ans += _2
        if ci+1 < N:
            arr[ci+1][cj] += _7
            arr[ci+1][cj+1] += _1
        else: ans += _7 + _1
        if ci+1 < N and 0 <= cj-1:  arr[ci+1][cj-1] += _10
        else:    ans += _10
        if ci+2 < N:    arr[ci+2][cj] += _2
        else:   ans += _2
        if 0 <= cj-2:   arr[ci][cj-2] += _5
        else:   ans += _5
        if cj-1 < 0:
            ans += arr[ci][cj]-(2*_10+2*_7+2*_2+2*_1+_5)
        else:
            arr[ci][cj-1] += (arr[ci][cj]-(2*_10+2*_7+2*_2+2*_1+_5))
    elif d == 1:
        if ci+2 < N:    arr[ci+2][cj] += _5
        else:   ans += _5
        if ci+1 < N and cj+1 < N:    arr[ci+1][cj+1] += _10
        else:   ans += _10
        if ci+1 < N and 0 <= cj-1:    arr[ci+1][cj-1] += _10
        else:   ans += _10
        if cj+1 < N:
            arr[ci][cj+1] += _7
            arr[ci-1][cj+1] += _1
        else:   ans += _7 + _1
        if cj+2 < N:    arr[ci][cj+2] += _2
        else:   ans += _2
        if 0 <= cj-1:
            arr[ci-1][cj-1] += _1
            arr[ci][cj-1] += _7
        else:   ans += _1 + _7
        if 0 <= cj-2:   arr[ci][cj-2] += _2
        else:   ans += _2
        if ci+1 >= N:
            ans += arr[ci][cj] - (2 * _10 + 2 * _7 + 2 * _2 + 2 * _1 + _5)
        else:
            arr[ci+1][cj] += (arr[ci][cj] - (2 * _10 + 2 * _7 + 2 * _2 + 2 * _1 + _5))
    elif d == 2:
        if 0 <= ci-1:
            arr[ci-1][cj] += _7
            arr[ci-1][cj-1] += _1
        else:   ans += _7 + _1
        if 0 <= ci-1 and cj+1 < N:  arr[ci-1][cj+1] += _10
        else:   ans += _10
        if 0 <= ci-2:
            arr[ci-2][cj] += _2
        else:   ans += _2
        if ci+1 < N:
            arr[ci+1][cj] += _7
            arr[ci+1][cj-1] += _1
        else:   ans += _7 + _1
        if ci+1 < N and cj+1 < N:   arr[ci+1][cj+1] += _10
        else:   ans += _10
        if ci+2 < N:    arr[ci+2][cj] += _2
        else:   ans += _2
        if cj+2 < N:   arr[ci][cj+2] += _5
        else:   ans += _5
        if cj+1 >= N:
            ans += arr[ci][cj] - (2 * _10 + 2 * _7 + 2 * _2 + 2 * _1 + _5)
        else:
            arr[ci][cj+1] += (arr[ci][cj] - (2 * _10 + 2 * _7 + 2 * _2 + 2 * _1 + _5))
    else:
        if 0 <= ci-2:   arr[ci-2][cj] += _5
        else:   ans += _5
        if 0 <= ci-1 and cj+1 < N:  arr[ci-1][cj+1] += _10
        else:   ans += _10
        if 0 <= ci-1 and 0 <= cj-1: arr[ci-1][cj-1] += _10
        else:   ans += _10
        if cj+1 < N:
            arr[ci][cj+1] += _7
            arr[ci+1][cj+1] += _1
        else:   ans += _7 + _1
        if cj+2 < N:    arr[ci][cj+2] += _2
        else:   ans += _2
        if 0 <= cj-1:
            arr[ci+1][cj-1] += _1
            arr[ci][cj-1] += _7
        else:   ans += _1 + _7
        if 0 <= cj-2:   arr[ci][cj-2] += _2
        else:   ans += _2
        if ci-1 < 0:
            ans += arr[ci][cj] - (2 * _10 + 2 * _7 + 2 * _2 + 2 * _1 + _5)
        else:
            arr[ci-1][cj] += (arr[ci][cj] - (2 * _10 + 2 * _7 + 2 * _2 + 2 * _1 + _5))


def tor(si, sj):
    ci, cj = si, sj
    d = 0
    # 최초 한 칸만 진행
    w = 0
    while True:
        w += 1
        # 마지막 한번의 이동만 남기고 break
        if w == N:
            break
        # w칸 전진은 2회 반복
        for k in range(2):
            # 한 방향으로 w만큼 전진
            for i in range(w):
                di, dj = delta[d]
                ni, nj = ci+di, cj+dj
                move(ni, nj, d)
                ci, cj = ni, nj
            # 방향 전환
            d = (d+1)%4

    # N-1회만큼 왼쪽으로 가면 끝
    for i in range(N-1):
        di, dj = delta[0]
        ni, nj = ci+di, cj+dj
        move(ni, nj, 0)
        ci, cj = ni, nj


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
si, sj = N//2, N//2
delta = ((0, -1), (1, 0), (0, 1), (-1, 0))
ans = 0
tor(si, sj)

print(ans)