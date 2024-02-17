import sys
sys.setrecursionlimit(10000)

def bfs(i ,j):
    v[i][j] = 1
    queue = [(i, j)]

    while queue:
        (ci, cj) = queue.pop(0)
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and graph[ni][nj] > k:
                queue.append((ni, nj))
                v[ni][nj] = 1

N = int(input())
graph = []
rain = 0

for i in range(N):
    lst = list(map(int, input().split()))
    rain = max(rain, max(lst))
    graph.append(lst)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
mx = 0

for k in range(rain+1):
    cnt = 0
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= k:
                continue
            if v[i][j] == 0:
                bfs(i, j)
                cnt += 1
    mx = max(cnt, mx)

print(mx)