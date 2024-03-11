from collections import deque

def rotate(l):
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            arr_T = list(zip(*[a[j:j+2**l] for a in arr[i:i+2**l]][::-1]))
            for ni in range(2**l):
                for nj in range(2**l):
                    arr[i+ni][j+nj] = arr_T[ni][nj]


def melt():
    m = []
    for i in range(2**N):
        for j in range(2**N):
            # 얼음이 아닌 칸은 넘어감
            if arr[i][j] == 0:
                continue
            cnt = 0
            for di, dj in delta:
                ni, nj = i+di, j+dj
                if 0 <= ni < 2**N and 0 <= nj < 2**N:
                    if arr[ni][nj] > 0:
                        cnt += 1
            # 얼음이 3면 이상 인접하지 않으면 1 감소
            if cnt < 3:
                m.append((i, j))

    # 동시에 녹음
    for mi, mj in m:
        arr[mi][mj] -= 1


def bfs(si, sj):
    global mx

    q = deque([(si, sj)])
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < 2**N and 0 <= nj < 2**N and not v[ni][nj] and arr[ni][nj]:
                v[ni][nj] = 1
                cnt += 1
                q.append((ni, nj))

    mx = max(mx, cnt)


N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
fs = list(map(int, input().split()))
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
# arr_T = list(zip(*arr[::-1]))
for l in fs:
    # l이 0이면 회전하지 않음
    if l:
        rotate(l)
    melt()

sm = 0
for lst in arr:
    sm += sum(lst)

v = [[0] * 2**N for _ in range(2**N)]
mx = 0
for i in range(2**N):
    for j in range(2**N):
        if arr[i][j] and not v[i][j]:
            v[i][j] = 1
            bfs(i, j)

print(sm)
print(mx)