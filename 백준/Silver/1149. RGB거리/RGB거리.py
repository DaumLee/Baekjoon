N = int(input())
# 전체 들어오는 입력 2차원 저장
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
# dp[0] = 첫 집을 칠하는 비용
dp[0] = arr[0]

# 위에서부터 하나씩 칠함
for i in range(1, N):
    for j in range(3):
        # 빨간 집을 칠함 + 이전에 초록색이나 파란집을 선택했을 때 까지의 비용
        if j == 0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + arr[i][j]
        # 초록 집을 선택
        elif j == 1:
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + arr[i][j]
        # 파란 집을 선택
        else:
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + arr[i][j]

print(min(dp[N-1]))