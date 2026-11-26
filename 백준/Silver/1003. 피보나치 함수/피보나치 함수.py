dp = [None] * 41
dp[0] = (1, 0)
dp[1] = (0, 1)

def fibo(n):
    if dp[n] is not None:
        return dp[n]

    a0, a1 = fibo(n-1)
    b0, b1 = fibo(n-2)
    dp[n] = (a0 + b0, a1 + b1)
    return dp[n]


T = int(input())

for tc in range(T):
    N = int(input())
    ans0, ans1 = fibo(N)
    print(ans0, ans1)