N, K = map(int, input().split())
# 무게는 0 ~ K까지 / 개수는 0 ~ N까지
dp = [[0] * (K+1) for _ in range(N+1)]

lst = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    w, v = lst[i-1]
    for j in range(1, K+1):
        # 더 들 수 없으면 이전과 동일
        if j < w:
            dp[i][j] = dp[i-1][j]
        # 더 들 수 있으면 현재 물품을 드는 것과 들지 않는 것의 최댓값을 비교
        else:
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])

print(dp[N][K])