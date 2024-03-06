def move(d, s, cur):

    # 구름 이동
    di, dj = delta[d]
    for c in range(len(cur)):
        cur[c] = (cur[c][0]+di*s)%N, (cur[c][1]+dj*s)%N

    # 바구니 채우기
    for ci, cj in cur:
        arr[ci][cj] += 1

    # 물 복사 버그
    for ci, cj in cur:
        for bi, bj in bug:
            ni, nj = ci+bi, cj+bj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                arr[ci][cj] += 1

    # 다음 구름의 위치
    nxt = []
    for i in range(N):
        for j in range(N):
            # 구름이 없던 칸에만 구름이 생길 수 있음
            if (i, j) in cur:
                continue
            if arr[i][j] >= 2:
                nxt.append([i, j])
                arr[i][j] -= 2

    return nxt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
# 대각선 버그 인덱스
bug = ((-1, -1), (1, 1), (-1, 1), (1, -1))

# 비바라기 시전
cloud = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]

for i in range(M):
    # d = 1~8
    d, s = map(int, input().split())
    # delta 배열과 인덱스 맞추기, d = 0 ~ 7
    d -= 1
    # 구름 이동
    cloud = move(d, s, cloud)

sm = 0
for lst in arr:
    sm += sum(lst)

print(sm)