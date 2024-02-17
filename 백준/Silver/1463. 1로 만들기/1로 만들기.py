X = int(input())
dp = [0, 0, 1, 1]

for n in range(4, X+1):
    dp.append(dp[n - 1] + 1)
    if not n % 3:
        dp[n] = min(dp[n], dp[n//3] + 1)
    if not n % 2:
        dp[n] = min(dp[n], dp[n//2] + 1)

print(dp[X])