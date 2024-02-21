from collections import deque


def bfs(s):
    global ans

    q = deque(s)
    v = [[0] * M for _ in range(N)]
    while q:
        si, sj = q.popleft()
        ci, cj = si, sj
        # 한칸씩 벌려나감
        for k in range(1, max(N, M)):
            cnt = 0
            for di, dj in delta:
                ni, nj = ci+di*k, cj+dj*k
                # 갈 수 있으면 체크
                if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == '*':
                    cnt += 1
            # 4방향 다 진행 가능하면 정답에 담음
            if cnt == 4:
                v[si][sj] = 1
                # 정답만 방문 처리
                for di, dj in delta:
                    ni, nj = ci+di*k, cj+dj*k
                    v[ni][nj] = 1
                ans.append((si+1, sj+1, k))
            else:
                break

    # 십자가를 전부 사용하지 않았다면 격자판을 만들 수 없음
    for i in start:
        if not v[i[0]][i[1]]:
            ans = []
            return


N, M = map(int, input().split())
graph = []
start = []
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
for i in range(N):
    lst = input()
    graph.append(lst)
    for j in range(M):
        if lst[j] == '*':
            start.append((i, j))

ans = []
bfs(start)
if ans:
    print(len(ans))
    # ans.sort(key=lambda x: (x[0], x[1], -x[2]))
    for item in ans:
        print(*item)
else:
    print(-1)