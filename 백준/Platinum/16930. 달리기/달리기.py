from collections import deque


def end_check(ei, ej):
    q = deque([(ei, ej)])
    v = [[0] * M for _ in range(N)]
    v[ei][ej] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            for k in range(1, K + 1):
                ni, nj = ci+di*k, cj+dj*k
                if 0 <= ni < N and 0 <= nj < M:
                    if v[ni][nj] or arr[ni][nj] == '#':
                        break
                    # 시작점에 도착할 수 있으면
                    if ni == si-1 and nj == sj-1:
                        return False
                    q.append((ni, nj))
                    v[ni][nj] = 1
                else:
                    break
    return True


def bfs(si, sj):
    q = deque([(si, sj)])
    v = [[-1] * M for _ in range(N)]
    v[si][sj] = 0

    while q:
        ci, cj = q.popleft()
        for d in range(4):
            # K번까지 갈 수 있고
            for k in range(1, K + 1):
                ni, nj = ci + delta[d][0] * k, cj + delta[d][1] * k
                # 범위 내에서
                if 0 <= ni < N and 0 <= nj < M:
                    # 벽을 만나면 해당 방향 전진 stop
                    if arr[ni][nj] == '#':
                        break
                    # 목적지를 만나면 종료
                    if ni == ei-1 and nj == ej-1:
                        return v[ci][cj] + 1
                    # 방문한 적 없거나 더 빠른 시간으로 도착 가능하면 전진 진행
                    if v[ni][nj] == -1 or v[ni][nj] > v[ci][cj] + 1:
                        v[ni][nj] = v[ci][cj] + 1
                        q.append((ni, nj))
                # 범위를 벗어나면 바로 다음 방향 순회
                else:
                    break


N, M, K = map(int, input().split())
arr = [input() for _ in range(N)]
si, sj, ei, ej = map(int, input().split())
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

if end_check(ei-1, ej-1):
    print(-1)
else:
    print(bfs(si-1, sj-1))