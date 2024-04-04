def check(ci, cj, cd):
    di, dj = delta[cd]
    ni, nj = ci+di, cj+dj
    if not (0 <= ni < N and 0 <= nj < N) or (arr[ni][nj] in blocked[cd]):
        return True
    return False


def find(si, sj, num):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == num and (i, j) != (si, sj):
                return i, j


def play(si, sj, cd):
    ci, cj = si, sj
    score = 0
    while True:
        di, dj = delta[cd]
        ni, nj = ci+di, cj+dj
        if (ni, nj) == (si, sj):
            return score
        if 0 <= ni < N and 0 <= nj < N:
            if not arr[ni][nj]:
                ci, cj = ni, nj
                continue
            elif 1 <= arr[ni][nj] <= 5:
                if arr[ni][nj] in blocked[cd]:
                    cd = (cd+2)%4
                else:
                    if arr[ni][nj] == turn[cd][0]:
                        cd = (cd+1)%4
                    else:
                        cd = (cd-1)%4
                ci, cj = ni, nj
                score += 1
            elif 6 <= arr[ni][nj] <= 10:
                ei, ej = find(ni, nj, arr[ni][nj])
                ci, cj = ei, ej
            else:
                return score
        else:
            cd = (cd+2)%4
            ci, cj = ni, nj
            score += 1


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    blocked = {0: (1, 2, 5), 1: (2, 3, 5), 2: (3, 4, 5), 3: (1, 4, 5)}
    turn = {0: (3, 4), 1: (4, 1), 2: (1, 2), 3: (2, 3)}
    ans = 0
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                for d in range(4):
                    if check(i, j, d) and check(i, j, (d+2)%4):
                        continue
                    ans = max(ans, play(i, j, d))
    print(f'#{tc} {ans}')