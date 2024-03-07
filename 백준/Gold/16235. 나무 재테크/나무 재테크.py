def earn(cur):
    nxt = [[list() for j in range(N)] for i in range(N)]

    # 봄
    for i in range(N):
        for j in range(N):
            # 나무가 있으면
            if cur[i][j]:
                for idx in range(len(cur[i][j])):
                    age = cur[i][j][idx]
                    # 양분 체크 후 다음 연도에 추가
                    if arr[i][j] >= age:
                        arr[i][j] -= age
                        nxt[i][j].append(age+1)
                    # 양분이 다 떨어졌으면 여름 진행
                    else:
                        for age in cur[i][j][idx:]:
                            arr[i][j] += age//2
                        break

    # 가을
    for i in range(N):
        for j in range(N):
            # 나무가 있으면
            if nxt[i][j]:
                for age in nxt[i][j]:
                    # 나이가 5의 배수면
                    if age%5 == 0:
                        for di, dj in delta:
                            ni, nj = i+di, j+dj
                            # 맨 앞에 나이가 1인 나무 추가
                            if 0 <= ni < N and 0 <= nj < N:
                                nxt[ni][nj] = [1] + nxt[ni][nj]

    #  겨울
    for i in range(N):
        for j in range(N):
            arr[i][j] += A[i][j]

    return nxt

N, M, K = map(int, input().split())
arr = [[5] * N for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[list() for j in range(N)] for i in range(N)]

delta = ((-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, -1), (1, 1), (1, 0))

for _ in range(M):
    i, j, k = map(int, input().split())
    tree[i-1][j-1].append(k)

# 최초 1회만 정렬
for i in range(N):
    for j in range(N):
        # 한 칸에 두 개 이상 나무가 있으면
        if len(tree[i][j]) >= 2:
            tree[i][j].sort()

for _ in range(K):
    tree = earn(tree)

sm = 0
for i in range(N):
    for j in range(N):
        sm += len(tree[i][j])

print(sm)