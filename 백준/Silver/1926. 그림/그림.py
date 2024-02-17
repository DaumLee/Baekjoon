from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and graph[ni][nj]:
                v[ni][nj] = 1
                cnt += 1
                q.append((ni, nj))
    ans.append(cnt)


N, M = map(int, input().split())
graph = [[0] * M for _ in range(N)]
pic = []
v = [[0] * M for _ in range(N)]
mx = 1
ans = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        graph[i][j] = lst[j]
        if lst[j]:
            pic.append((i, j))

for i in range(len(pic)):
    if not v[pic[i][0]][pic[i][1]]:
        bfs(pic[i][0], pic[i][1])

print(len(ans))
if not ans:
    print(0)
else:
    print(max(ans))