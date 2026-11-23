MAX = 14
dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for n in range(1, MAX + 1):
    dp[0][n] = n

for k in range(1, MAX + 1):
    for n in range(1, MAX + 1):
        dp[k][n] = dp[k][n - 1] + dp[k - 1][n]


def solve(k, n):
    print(dp[k][n])


for t in range(1, int(input()) + 1):
    k = int(input())
    n = int(input())
    solve(k, n)