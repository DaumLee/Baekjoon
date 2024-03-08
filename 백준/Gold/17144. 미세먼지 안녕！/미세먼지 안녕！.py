def up(si):
    ci, cj = ref[0][0]-1, 0
    for d in range(4):
        di, dj = delta[d]
        while True:
            ni, nj = ci+di, cj+dj
            if d == 0 and ni < 0:
                break
            elif d == 1 and nj > M-1:
                break
            elif d == 2 and ni > si:
                break
            elif d == 3 and nj < 0:
                break
            arr[ci][cj] = arr[ni][nj]
            ci, cj = ni, nj


def down(si):
    ci, cj = ref[1][0]+1, 0
    for d in range(3,-1,-1):
        d = (d-1)%4
        di, dj = delta[d]
        while True:
            ni, nj = ci+di, cj+dj
            if d == 0 and ni < si:
                break
            elif d == 1 and nj > M-1:
                break
            elif d == 2 and ni > N-1:
                break
            elif d == 3 and nj < 0:
                break
            arr[ci][cj] = arr[ni][nj]
            ci, cj = ni, nj


def bfs(d):
    # 확산될 미세먼지
    v = [[0] * M for _ in range(N)]

    for ci, cj in d:
        cnt = 0
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj
            # 공청기가 없는 칸으로 확산
            if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in ref:
                v[ni][nj] += arr[ci][cj]//5
                cnt += 1
        v[ci][cj] -= (arr[ci][cj]//5)*cnt

    # 최종 미세먼지 동시 확산 처리
    for i in range(N):
        for j in range(M):
            arr[i][j] += v[i][j]


N, M, T = map(int, input().split())
arr = []
ref = []
dust = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        # 공청기
        if lst[j] == -1:
            ref.append((i, j))
            lst[j] = 0
        # 미세먼지
        elif lst[j]:
            dust.append((i, j))
    arr.append(lst)

# 위, 오른쪽, 아래, 왼쪽
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

for _ in range(T):
    # 미세먼지 확산
    bfs(dust)
    arr[ref[0][0]-1][0] = 0
    arr[ref[1][0]+1][0] = 0
    # 공기청정기
    up(ref[0][0])
    down(ref[1][0])
    dust = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                dust.append((i, j))

sm = 0
for i in range(N):
    sm += sum(arr[i])

print(sm)