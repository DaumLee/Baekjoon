from collections import deque


def find(si, sj, std):
    q = deque([(si, sj)])
    lst = [(si, sj)]
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < 12 and 0 <= nj < 6 and not v[ni][nj] and arr[ni][nj] == std:
                lst.append((ni, nj))
                q.append((ni, nj))
                v[ni][nj] = 1
    if len(lst) >= 4:
        return lst
    else:
        return []


arr = [list(input()) for _ in range(12)]
time = 0
while True:
    v = [[0] * 6 for _ in range(12)]
    bomb = []
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and not v[i][j]:
                v[i][j] = 1
                bomb += find(i, j, arr[i][j])
    if bomb:
        for ci, cj in bomb:
            arr[ci][cj] = '.'
        for _ in range(12):
            for i in range(11, 0, -1):
                for j in range(6):
                    if arr[i][j] == '.':
                        arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
        time += 1
    else:
        break
print(time)