from collections import defaultdict, deque


def fn1():
    for ac in aircon:
        v = [[0] * M for _ in range(N)]
        ai, aj, ad = ac
        di, dj = delta[ad]
        ni, nj = ai+di, aj+dj
        air = 5
        arr[ni][nj] += air
        q = deque([(ni, nj)])
        if ad == 1:
            while q:
                air -= 1
                if not air: break
                for _ in range(len(q)):
                    ci, cj = q.popleft()
                    if cj == M-1: q = []; break
                    if ci >= 1 and (ci-1, cj) not in wall[(ci, cj)] and (ci-1, cj+1) not in wall[(ci-1, cj)] and not v[ci-1][cj+1]:
                        v[ci-1][cj+1] = 1
                        q.append((ci-1, cj+1))
                        arr[ci-1][cj+1] += air
                    if (ci, cj+1) not in wall[(ci, cj)] and not v[ci][cj+1]:
                        v[ci][cj+1] = 1
                        q.append((ci, cj+1))
                        arr[ci][cj+1] += air
                    if ci < N-1 and (ci+1, cj) not in wall[(ci, cj)] and (ci+1, cj+1) not in wall[(ci+1, cj)] and not v[ci+1][cj+1]:
                        v[ci+1][cj+1] = 1
                        q.append((ci+1, cj+1))
                        arr[ci+1][cj+1] += air
        elif ad == 2:
            while q:
                air -= 1
                if not air: break
                for _ in range(len(q)):
                    ci, cj = q.popleft()
                    if cj == 0: q = []; break
                    if ci >= 1 and (ci-1, cj) not in wall[(ci, cj)] and (ci-1, cj-1) not in wall[(ci-1, cj)] and not v[ci-1][cj-1]:
                        v[ci-1][cj-1] = 1
                        q.append((ci-1, cj-1))
                        arr[ci-1][cj-1] += air
                    if (ci, cj-1) not in wall[(ci, cj)] and not v[ci][cj-1]:
                        v[ci][cj-1] = 1
                        q.append((ci, cj-1))
                        arr[ci][cj-1] += air
                    if ci < N-1 and (ci+1, cj) not in wall[(ci, cj)] and (ci+1, cj-1) not in wall[(ci+1, cj)] and not v[ci+1][cj-1]:
                        v[ci+1][cj-1] = 1
                        q.append((ci+1, cj-1))
                        arr[ci+1][cj-1] += air
        elif ad == 3:
            while q:
                air -= 1
                if not air: break
                for _ in range(len(q)):
                    ci, cj = q.popleft()
                    if ci == 0: q = []; break
                    if cj >= 1 and (ci, cj-1) not in wall[(ci, cj)] and (ci-1, cj-1) not in wall[(ci, cj-1)] and not v[ci-1][cj-1]:
                        v[ci-1][cj-1] = 1
                        q.append((ci-1, cj-1))
                        arr[ci-1][cj-1] += air
                    if (ci-1, cj) not in wall[(ci, cj)] and not v[ci-1][cj]:
                        v[ci-1][cj] = 1
                        q.append((ci-1, cj))
                        arr[ci-1][cj] += air
                    if cj < M-1 and (ci, cj+1) not in wall[(ci, cj)] and (ci-1, cj+1) not in wall[(ci, cj+1)] and not v[ci-1][cj+1]:
                        v[ci-1][cj+1] = 1
                        q.append((ci-1, cj+1))
                        arr[ci-1][cj+1] += air
        else:
            while q:
                air -= 1
                if not air: break
                for _ in range(len(q)):
                    ci, cj = q.popleft()
                    if ci == N-1: q = []; break
                    if cj >= 1 and (ci, cj-1) not in wall[(ci, cj)] and (ci+1, cj-1) not in wall[(ci, cj-1)] and not v[ci+1][cj-1]:
                        v[ci+1][cj-1] = 1
                        q.append((ci+1, cj-1))
                        arr[ci+1][cj-1] += air
                    if (ci+1, cj) not in wall[(ci, cj)] and not v[ci+1][cj]:
                        v[ci+1][cj] = 1
                        q.append((ci+1, cj))
                        arr[ci+1][cj] += air
                    if cj < M-1 and (ci, cj+1) not in wall[(ci, cj)] and (ci+1, cj+1) not in wall[(ci, cj+1)] and not v[ci+1][cj+1]:
                        v[ci+1][cj+1] = 1
                        q.append((ci+1, cj+1))
                        arr[ci+1][cj+1] += air


def fn2():
    nxt = [lst[:] for lst in arr]
    for i in range(N):
        for j in range(M):
            if i < N-1:
                if arr[i][j] != arr[i+1][j]:
                    if (i+1, j) not in wall[(i, j)]:
                        df = abs(arr[i][j]-arr[i+1][j])
                        if arr[i][j] > arr[i+1][j]:
                            nxt[i][j] -= df//4
                            nxt[i+1][j] += df//4
                        else:
                            nxt[i+1][j] -= df//4
                            nxt[i][j] += df//4
            if j < M-1:
                if arr[i][j] != arr[i][j+1]:
                    if (i, j+1) not in wall[(i, j)]:
                        df = abs(arr[i][j]-arr[i][j+1])
                        if arr[i][j] > arr[i][j+1]:
                            nxt[i][j] -= df//4
                            nxt[i][j+1] += df//4
                        else:
                            nxt[i][j+1] -= df//4
                            nxt[i][j] += df//4

    for i in (0, N-1):
        for j in range(M):
            if nxt[i][j]:
                nxt[i][j] -= 1
    for j in (0, M-1):
        for i in range(1, N-1):
            if nxt[i][j]:
                nxt[i][j] -= 1
    return nxt


N, M, K = map(int, input().split())
arr = []
aircon = []
end = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if 1 <= lst[j] <= 4:
            aircon.append((i, j, lst[j]))
            lst[j] = 0
        elif lst[j] == 5:
            end.append((i, j))
            lst[j] = 0
    arr.append(lst)
wall = defaultdict(list)
W = int(input())
for _ in range(W):
    x, y, s = map(int, input().split())
    x, y = x-1, y-1
    if s == 0:
        wall[(x, y)].append((x-1, y))
        wall[(x-1, y)].append((x, y))
    else:
        wall[(x, y)].append((x, y+1))
        wall[(x, y+1)].append((x, y))
delta = {2: (0, -1), 3: (-1, 0), 1: (0, 1), 4: (1, 0)}
for time in range(0, 102):
    for ei, ej in end:
        if arr[ei][ej] < K: break
    else: break
    fn1()
    arr = fn2()
    continue
if time > 100:
    print(101)
else:
    print(time)