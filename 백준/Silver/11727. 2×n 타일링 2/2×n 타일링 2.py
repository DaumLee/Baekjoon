n = int(input())
dp = [0, 1, 3]
for i in range(3, n+1):
    dp.append(0)
    if i % 2:
        dp[i] = 1 + 2*(dp[i-1]-1)
    else:
        # 전체가 1인 경우 하나 빼고 x2 경우 / 전체를 2블록으로 채우는 경우 / 사이에 끼는 경우
        dp[i] = 2*(dp[i-1]-1) + 1 + 1 + 1

print(dp[n] % 10007)