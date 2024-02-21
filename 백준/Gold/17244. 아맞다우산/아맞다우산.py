from collections import deque


# (si, sj) ~ (ei, ej)의 거리
def bfs(si, sj, ei, ej):
    q = deque([(si, sj)])
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if ni == ei and nj == ej:
                return v[ci][cj]
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and graph[ni][nj] != '#':
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1


def solve(n, ci, cj, d):
    global dist, ei, ej

    # 이미 거리가 최소보다 멀리 갔으면 종료
    if d >= dist:
        return

    # 모든 거점을 방문했으면
    if n == len(m):
        # 마지막 거점에서 목적지까지 거리를 더한 후 최소거리 체크
        dist = min(dist, d+bfs(ci, cj, ei, ej))
        return

    for i in range(len(m)):
        # 방문하지 않았던 거점을 방문 처리하고 거리를 추가
        if not v[i]:
            v[i] = 1
            solve(n+1, m[i][0], m[i][1], d+bfs(ci, cj, m[i][0], m[i][1]))
            v[i] = 0


M, N = map(int, input().split())
graph = []
m = []
for i in range(N):
    lst = input()
    graph.append(lst)
    for j in range(M):
        if lst[j] == 'S':
            si, sj = i, j
        elif lst[j] == 'E':
            ei, ej = i, j
        elif lst[j] == 'X':
            m.append((i, j))

m.sort(key=lambda x: abs(si-x[0])+abs(sj-x[1]))
# 거점 방문 체크
v = [0]*len(m)
# 최악의 거리
dist = N * M
solve(0, si, sj, 0)

print(dist)