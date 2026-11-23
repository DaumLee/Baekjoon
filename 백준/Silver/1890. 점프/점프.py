def bfs(si, sj):
    dp = [[0] * N for _ in range(N)]
    dp[si][sj] = 1

    for ci in range(si, N):
        for cj in range(sj, N):
            # 도달할 수 없거나 도착점이면 건너뜀
            if not dp[ci][cj] or (ci == N-1 and cj == N-1):
                continue
            # 칸에 적힌 수 만큼 이동
            k = arr[ci][cj]
            # 0이 적혀 있으면 더 진행 불가능
            if k == 0:
                continue
            for di, dj in delta:
                ni, nj = ci+di*k, cj+dj*k
                # 숫자가 줄어들지 않기 때문에 0 비교 X
                if ni < N and nj < N:
                    dp[ni][nj] += dp[ci][cj]

    return dp[N-1][N-1]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 오른쪽, 아래로만 이동
delta = ((0, 1), (1, 0))

print(bfs(0, 0))