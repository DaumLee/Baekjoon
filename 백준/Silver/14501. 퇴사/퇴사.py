# n일, 금액 합계
def solve(n, sm):
    global ans

    if ans < sm:
        ans = sm

    # 마지막 날에는 상담 불가능
    if n >= N:
        return

    for i in range(n+1, N):
        # 진행할 수 있으면
        if i + lst[i][2]-1 < N and not v[n]:
            v[n] = 1
            solve(i+lst[i][2]-1, sm+lst[i][0])
            v[n] = 0


N = int(input())
lst = []
for i in range(N):
    t, p = map(int, input().split())
    lst.append((p, i, t))

v = [0] * N
ans = 0
solve(-1, 0)
print(ans)