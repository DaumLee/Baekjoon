from collections import deque

def check(start, num):
    for si, sj, _ in start:
        v[si][sj] = num
    q = deque(start)
    cnt = 0
    while q:
        ci, cj, time = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and v[ni][nj] != num:
                v[ni][nj] = num
                if not arr[ni][nj]:
                    cnt += 1
                    if cnt == virus:
                        return time+1
                q.append((ni, nj, time+1))
    return N**2+1


def find(n, lst):
    global ans, num

    if len(lst) == M:
        ans = min(ans, check(lst, num))
        num += 1
        return

    for i in range(n+1, len(hp)):
        find(i, lst+[hp[i]])


delta = ((-1, 0), (1, 0), (0, 1), (0, -1))
N, M = map(int, input().split())
v = [[0] * N for _ in range(N)]
num = 1
arr = []
hp = []
virus = 0
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 0:
            virus += 1
        if lst[j] == 2:
            hp.append((i, j, 0))
    arr.append(lst)
if not virus:
    print(0)
else:
    ans = N ** 2 + 1
    find(-1, [])
    if ans == N**2+1:
        print(-1)
    else:
        print(ans)