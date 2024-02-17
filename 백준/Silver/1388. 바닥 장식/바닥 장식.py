def dfs0(si, sj):
    v[si][sj] = 1

    ni = si
    nj = sj + 1
    if 0 <= nj < M and graph[si][sj] == graph[ni][nj] and not v[ni][nj]:
        dfs0(ni, nj)


def dfs1(si, sj):
    v[si][sj] = 1

    ni = si + 1
    nj = sj
    if 0 <= ni < N and graph[si][sj] == graph[ni][nj] and not v[ni][nj]:
        dfs1(ni, nj)


N, M = map(int, input().split())
graph = []
cnt = 0
v = [[0] * M for _ in range(N)]

for _ in range(N):
    lst = list(input())
    for i in range(M):
        if lst[i] == '-':
            lst[i] = 0
        else:
            lst[i] = 1
    graph.append(lst)

for i in range(N):
    for j in range(M):
        if v[i][j]:
            continue
        if graph[i][j] == 0:
            dfs0(i, j)
            cnt += 1
        else:
            dfs1(i, j)
            cnt += 1

print(cnt)