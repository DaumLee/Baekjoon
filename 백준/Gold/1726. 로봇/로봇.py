from collections import deque


def turn(cd, time):
    if cd == ed:
        return time
    elif (cd-1)%4 == ed or (cd+1)%4 == ed:
        return time+1
    else:
        return time+2


def bfs(si, sj, sd):
    q = deque([(si, sj, sd, 0)])
    v = [[0] * M for _ in range(N)]
    dir = [[[] for j in range(M)] for i in range(N)]
    v[si][sj] = 1

    while q:
        ci, cj, cd, time = q.popleft()
        if ci == ei-1 and cj == ej-1:
            return turn(cd, time)
        # go
        for di, dj in delta[cd]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
                # 장애물을 만나면 더 나아갈 수 없음
                if arr[ni][nj] == 1:
                    break
                v[ni][nj] = 1
                q.append((ni, nj, cd, time+1))
        # turn left
        ld = (cd+1)%4
        # 해당 방향으로 진행한 적 없으면
        if ld not in dir[ci][cj]:
            dir[ci][cj].append(ld)
            q.append((ci, cj, ld, time+1))
        # turn right
        rd = (cd-1) % 4
        # 해당 방향으로 진행한 적 없으면
        if rd not in dir[ci][cj]:
            dir[ci][cj].append(rd)
            q.append((ci, cj, rd, time+1))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 동 북 서 남
delta = (
    ((0, 1), (0, 2), (0, 3)),
    ((-1, 0), (-2, 0), (-3, 0)),
    ((0, -1), (0, -2), (0, -3)),
    ((1, 0), (2, 0), (3, 0)),
)

si, sj, sd = map(int, input().split())
ei, ej, ed = map(int, input().split())

# rule-based 방향 변경
if sd == 1:
    sd = 0
elif sd == 4:
    sd = 1

# rule-based 방향 변경
if ed == 1:
    ed = 0
elif ed == 4:
    ed = 1

print(bfs(si-1, sj-1, sd))