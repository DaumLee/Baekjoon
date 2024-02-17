from collections import deque


def air(si, sj):
    v = [[0] * M for _ in range(N)]
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1
    graph[si][sj] = 2

    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and (graph[ni][nj] == 0 or graph[ni][nj] == 2):
                graph[ni][nj] = 2
                v[ni][nj] = 1
                q.append((ni, nj))


def melt():
    global cnt

    m = []
    for ci in range(N):
        for cj in range(M):
            if graph[ci][cj] == 1:
                chz = 0
                for di, dj in d:
                    ni, nj = ci+di, cj+dj
                    if graph[ni][nj] == 2:
                        chz += 1
                if chz >= 2:
                    m.append((ci, cj))
    for idx in range(len(m)):
        graph[m[idx][0]][m[idx][1]] = 2
        cnt -= 1


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
# 지우는  횟수
ans = 0
# 치즈 개수 세기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cnt += 1

# 사방
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
# 외부 공기는 2로 바꿈(0,0이 무조건 0이라 여기서부터 bfs)
air(0, 0)
while cnt:
    ans += 1
    melt()
    # 치즈가 녹아 외부 공기가 추가될 수 있음
    air(0, 0)

print(ans)