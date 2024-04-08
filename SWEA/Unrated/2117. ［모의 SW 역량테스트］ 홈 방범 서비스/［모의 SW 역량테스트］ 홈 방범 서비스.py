from collections import deque


def bfs(si, sj):
    global ans
    q = deque([(si, sj)])
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    cnt = arr[si][sj]
    k = 1
    while q:
        k += 1
        if k == 22: break
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ni, nj = ci+di, cj+dj
                if 0 <= ni < N and 0 <= nj < N and not v[ni][nj]:
                    v[ni][nj] = 1
                    q.append((ni, nj))
                    if arr[ni][nj]:
                        cnt += 1
        if cnt*M >= cost[k]:
            ans = max(ans, cnt)


cost = {2: 5, 3: 13, 4: 25, 5: 41, 6: 61, 7: 85, 8: 113, 9: 145, 10: 181, 11: 221, 12: 265, 13: 313, 14: 365, 15: 421, 16: 481, 17: 545, 18: 613, 19: 685, 20: 761, 21: 841}
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 1
    flag = 0
    for i in range(N):
        for j in range(N):
            bfs(i, j)
    print(f'#{tc} {ans}')