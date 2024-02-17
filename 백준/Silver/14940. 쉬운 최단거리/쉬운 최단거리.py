import sys
from collections import deque
input = sys.stdin.readline


def bfs(si, sj):
    q = deque([(si, sj)])
    v = [[0] * M for _ in range(N)]

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and graph[ni][nj] and not (ni == si and nj == sj):
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))

    for i in range(len(v)):
        for j in range(len(v[i])):
            if v[i][j] == 0 and graph[i][j] and not (i == si and j == sj):
                v[i][j] = -1

    for line in v:
        print(*line)

N, M = map(int, input().split())
graph = []
flag = 1
for i in range(N):
    lst = list(map(int, input().split()))
    graph.append(lst)
    if flag:
        for j in range(M):
            if lst[j] == 2:
                si, sj = i, j
                flag = 0

bfs(si, sj)