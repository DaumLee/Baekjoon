def check(clst):
    global ans

    tmp = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(len(cctv)):
        ci, cj = cctv[i]
        d = clst[i]
        if arr[ci][cj] == 1:
            di, dj = cctv1[d]
            for k in range(1, mx):
                ni, nj = ci+di*k, cj+dj*k
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] == 6:
                        break
                    if arr[ni][nj] != 0 or tmp[ni][nj]:
                        continue
                    tmp[ni][nj] = 1
                    cnt += 1
        elif arr[ci][cj] == 2:
            for di, dj in cctv2[d]:
                for k in range(1, mx):
                    ni, nj = ci + di * k, cj + dj * k
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 6:
                            break
                        if arr[ni][nj] != 0 or tmp[ni][nj]:
                            continue
                        tmp[ni][nj] = 1
                        cnt += 1
        elif arr[ci][cj] == 3:
            for di, dj in cctv3[d]:
                for k in range(1, mx):
                    ni, nj = ci + di * k, cj + dj * k
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 6:
                            break
                        if arr[ni][nj] != 0 or tmp[ni][nj]:
                            continue
                        tmp[ni][nj] = 1
                        cnt += 1
        elif arr[ci][cj] == 4:
            for di, dj in cctv4[d]:
                for k in range(1, mx):
                    ni, nj = ci + di * k, cj + dj * k
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 6:
                            break
                        if arr[ni][nj] != 0 or tmp[ni][nj]:
                            continue
                        tmp[ni][nj] = 1
                        cnt += 1
        elif arr[ci][cj] == 5:
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                for k in range(1, mx):
                    ni, nj = ci + di * k, cj + dj * k
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 6:
                            break
                        if arr[ni][nj] != 0 or tmp[ni][nj]:
                            continue
                        tmp[ni][nj] = 1
                        cnt += 1

    ans = max(ans, cnt)


def solve(n, clst):
    if n == len(cctv):
        check(clst)
        return

    for d in range(cctv_dir[n]):
        solve(n+1, clst+[d])


N, M = map(int, input().split())
mx = max(N, M)
arr = []
cctv = []
wall = []
# 전체 크기
size = 0
for i in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)
    for j in range(M):
        if 1 <= lst[j] <= 5:
            cctv.append((i, j))
        elif lst[j] == 0:
            size += 1

# 안전지역 크기
safe = 0

cctv1 = ((0, 1), (0, -1), (1, 0), (-1, 0))
cctv2 = (((0, 1), (0, -1)), ((1, 0), (-1, 0)))
cctv3 = (((0, -1), (1, 0)), ((1, 0), (0, 1)), ((0, 1), (-1, 0)), ((0, -1), (-1, 0)))
cctv4 = (((0, -1), (1, 0), (-1, 0)), ((1, 0), (0, 1), (0, -1)), ((0, 1), (-1, 0), (1, 0)), ((0, -1), (-1, 0), (0, 1)))
cctv5 = ((0, 1), (0, -1), (1, 0), (-1, 0))


# cctv가 감시할 수 있는 방향 순서대로 체크
cctv_dir = []
for ci, cj in cctv:
    if arr[ci][cj] == 1 or arr[ci][cj] == 3 or arr[ci][cj] == 4:
        cctv_dir.append(4)
    elif arr[ci][cj] == 2:
        cctv_dir.append(2)
    else:
        cctv_dir.append(1)

# 단계별 최대 안전영역 크기 저장
ans = 0
solve(0, [])
print(size-(safe+ans))