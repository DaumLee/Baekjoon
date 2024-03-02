def solve(n, v, s):
    global mx

    for j in range(n+1, N):
        d = dice[j]
        # 지금 주사위의 밑면 인덱스를 찾고
        idx = d.index(v)
        # 인덱스가 홀수면
        if idx % 2:
            d = dice[j][idx-1:] + dice[j][:idx-1]
            # 0번째가 윗면
            v = d[0]
        # 인덱스가 짝수면
        else:
            d = dice[j][idx:] + dice[j][:idx]
            # 1번째가 윗면
            v = d[1]
        s += max(d[2:])

    mx = max(mx, s)


N = int(input())

dice = []
for _ in range(N):
    a, b, c, d, e, f = (map(int, input().split()))
    # 0,1 / 2,3 / 4,5가 마주 보는 면
    dice.append((a, f, b, d, c, e))

mx = 0

# 하나씩 밑면에 두고 진행해봄
for i in range(0, 5, 2):
    d = dice[0][i:]+dice[0][:i]
    sm = max(d[2:])
    # 주사위 번호, 윗면 값, 합계
    solve(0, d[0], sm)
    solve(0, d[1], sm)

print(mx)