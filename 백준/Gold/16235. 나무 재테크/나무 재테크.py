from collections import deque

N, M, K = map(int, input().split())
virus = [[deque() for _ in range(N)] for _ in range(N)]
delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
plus = [list(map(int, input().split())) for _ in range(N)]
arr = [[5] * N for _ in range(N)]

for _ in range(M):
    si, sj, age = map(int, input().split())
    si, sj = si-1, sj-1
    virus[si][sj].append(age)

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if virus[i][j]:
                nxt = deque()
                while virus[i][j]:
                    v = virus[i][j].popleft()
                    if arr[i][j] >= v:
                        arr[i][j] -= v
                        nxt.append(v+1)
                    else:
                        arr[i][j] += v // 2
                        while virus[i][j]:
                            v = virus[i][j].popleft()
                            arr[i][j] += v//2
                        break
                virus[i][j] = nxt
    for i in range(N):
        for j in range(N):
            if virus[i][j]:
                for idx in range(len(virus[i][j])):
                    tree = virus[i][j][idx]
                    if tree%5 == 0:
                        for di, dj in delta:
                            ni, nj = i+di, j+dj
                            if 0 <= ni < N and 0 <= nj < N:
                                virus[ni][nj].appendleft(1)
    for i in range(N):
        for j in range(N):
            arr[i][j] += plus[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(virus[i][j])
print(ans)