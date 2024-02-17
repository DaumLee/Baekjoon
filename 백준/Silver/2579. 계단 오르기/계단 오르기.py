N = int(input())
lst = [int(input()) for _ in range(N)]

# 인덱스 = [연속으로 밟은 칸 수-1][현재 칸 번호-1]
dp = [[0 for j in range(N)] for i in range(2)]
# 1칸 연속해서 밟은 맨 첫칸
dp[0][0] = lst[0]
if N > 1:
    dp[0][1] = lst[1]

for i in range(1, N):
    # 연속된 칸을 밟는 경우엔 이전 계단 점수 + 지금 칸 점수
    dp[1][i] = dp[0][i-1] + lst[i]
    if i >= 2:
        # 두 칸 뛰면 연속 칸 수 초기화
        dp[0][i] = max(dp[1][i-2], dp[0][i-2]) + lst[i]

print(max(dp[0][-1], dp[1][-1]))