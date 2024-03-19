from collections import deque

def bfs_to_goal(si, sj, ei, ej):
    q = deque([(si, sj)])
    v = [[0] * (N+2) for _ in range(N+2)]
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        if ci == ei and cj == ej:
            return v[ci][cj]-1
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci + di, cj + dj
            # 장애물이 아니면
            if arr[ni][nj] != 1 and not v[ni][nj]:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
    return -1

def bfs(si, sj):
    q = deque([(si, sj)])
    v = [[0] * (N+2) for _ in range(N+2)]
    v[si][sj] = 1
    # 태울 후보 선정
    ai = aj = N+1
    # 최대 길이
    flag = N**2
    while q:
        ci, cj = q.popleft()
        if v[ci][cj] > flag:
            break
        if arr[ci][cj] >= 2:
            if ci < ai or ci == ai and cj < aj:
                ai, aj = ci, cj
            flag = v[ci][cj]
            continue
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci+di, cj+dj
            # 장애물이 아니면
            if arr[ni][nj] != 1 and not v[ni][nj]:
                v[ni][nj] = v[ci][cj]+1
                q.append((ni, nj))
    # 다른 승객을 태우러 갈 수 없으면
    if flag == N**2:
        return -1, -1, -1, -1
    # 승객까지 가는데 사용한 배터리
    bat1 = v[ai][aj]-1
    ei, ej = goal[arr[ai][aj]]
    arr[ai][aj] = 0
    # 승객을 태워 보내는 데 사용한 배터리
    bat2 = bfs_to_goal(ai, aj, ei, ej)
    # 승객을 태우고 도착지에 도착할 수 없으면
    if bat2 == -1:
        # 수정 (2시 29분)
        return -1, -1, -1, -1
    return ei, ej, bat1, bat2

N, M, K = map(int, input().split())
arr = [[1] * (N+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]
goal = dict()
cnt = 0
si, sj = map(int, input().split())
for i in range(2, M+2):
    ci, cj, ei, ej = map(int, input().split())
    arr[ci][cj] = i
    goal[i] = (ei, ej)
    cnt += 1

# 가용 배터리
b = K
while cnt:
    # 시작 칸, 사용 배터리
    si, sj, bat1, bat2 = bfs(si, sj)
    if si == -1:
        print(-1)
        break
    # 배터리 사용량을 넘기면 불가능
    if b-(bat1+bat2) < 0:
        print(-1)
        break
    # 충전
    b -= bat1
    b += bat2
    cnt -= 1
else:
    print(b)