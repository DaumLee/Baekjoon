def popped(a, si, sj, sp):
    for d in range(4):
        di, dj = delta[d]
        for k in range(sp-1):
            if k == 0:
                ci, cj = si, sj
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if a[ni][nj]:
                    np = a[ni][nj]
                    a[ni][nj] = 0
                    popped(a, ni, nj, np)
                ci, cj = ni, nj
            else:
                break


def gravity(a):
    for j in range(M):
        for i in range(N-1, -1, -1):
            if a[i][j]:
                ci = i
                while True:
                    ni = ci+1
                    if ni < N and a[ni][j]:
                        a[i][j], a[ni-1][j] = a[ni-1][j], a[i][j]
                        break
                    if ni == N-1 and not a[ni][j]:
                        a[i][j], a[ni][j] = a[ni][j], a[i][j]
                        break
                    elif ni < N and not a[ni][j]:
                        ci = ni
                    else:
                        break


def play(lst):
    a = [lst[:] for lst in arr]
    for num in lst:
        flag = 0
        for i in range(N):
            if a[i][num]:
                flag = 1
                sp = a[i][num]
                a[i][num] = 0
                popped(a, i, num, sp)
                break
        if not flag:
            break
        gravity(a)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if a[i][j]:
                cnt += 1
    return cnt


def find(lst):
    global ans
    if ans == 0:
        return
    if len(lst) == K:
        score = play(lst)
        if score != -1:
            ans = min(ans, score)
        return

    for i in range(M):
        find(lst + [i])


delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
for tc in range(1, int(input()) + 1):
    K, M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = N * M
    find([])
    print(f'#{tc} {ans}')