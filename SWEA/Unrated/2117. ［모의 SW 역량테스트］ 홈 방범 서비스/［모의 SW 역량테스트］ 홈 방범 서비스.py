from collections import deque


def bfs(si, sj, k):
    q = deque([(si, sj)])
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    cnt = 0
    if arr[si][sj]:
        cnt += 1
    while q:
        for _ in range(len(q)):
            ci, cj = q.popleft()
            if v[ci][cj] >= k:
                return cnt
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ni, nj = ci+di, cj+dj
                if 0 <= ni < N and 0 <= nj < N and not v[ni][nj]:
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni, nj))
                    if arr[ni][nj]:
                        cnt += 1
    return cnt


cost = {2: 5, 3: 13, 4: 25, 5: 41, 6: 61, 7: 85, 8: 113, 9: 145, 10: 181, 11: 221, 12: 265, 13: 313, 14: 365, 15: 421, 16: 481, 17: 545, 18: 613, 19: 685, 20: 761, 21: 841}
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = sum(map(sum, arr))
    ans = 1
    flag = 0
    for K in range(2, min(22, N+2)):
        for i in range(N):
            for j in range(N):
                cnt = bfs(i, j, K)
                if cnt*M >= cost[K]:
                    ans = max(ans, cnt)
                    if ans == mx:
                        flag = 1
                        break
            if flag:
                break
        if flag:
            break
    print(f'#{tc} {ans}')