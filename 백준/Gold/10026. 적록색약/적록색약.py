import sys
sys.setrecursionlimit(10000)

def dfs(i ,j):
    v[i][j] = 1

    for di, dj in d:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if v[ni][nj] == 1:
                continue
            if graph[ni][nj] == graph[i][j]:
                dfs(ni, nj)

N = int(input())
graph = [list(input()) for _ in range(N)]
v = [[0] * N for _ in range(N)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if v[i][j] == 0:
            dfs(i, j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

v = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if v[i][j] == 0:
            dfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)