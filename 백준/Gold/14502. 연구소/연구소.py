from collections import deque


def scoring(added, num):
    tmp = [lst[:] for lst in arr]
    for wi, wj in added:
        tmp[wi][wj] = 1
    q = deque(fire)
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] != num and not tmp[ni][nj]:
                v[ni][nj] = num
                q.append((ni, nj))
    ret = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] == num:
                ret += 1
    return ret


def solve(ci, cj, lst=[]):
    global score, num
    if len(lst) == 3:
        score = min(score, scoring(lst, num))
        num += 1
        return

    for i in range(ci, N):
        for j in range(M):
            if i == ci and j <= cj: continue
            if not arr[i][j]:
                solve(i, j, lst+[(i, j)])


N, M = map(int, input().split())
arr = []
fire = []
v = [[0] * M for _ in range(N)]
blanks = 0
for i in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)
    for j in range(M):
        if lst[j] == 2:
            fire.append((i, j))
        elif lst[j] == 0:
            blanks += 1
num = 1
score = N*M
solve(-1, -1)
print(blanks-score-3)