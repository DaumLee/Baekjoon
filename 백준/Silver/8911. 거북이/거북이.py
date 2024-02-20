delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

for _ in range(int(input())):
    st = list(input())
    # 초기값 세팅
    ci = cj = mx_i = mn_i = mx_j = mn_j = 0
    # 방향 변수
    d = 0

    for order in st:
        if order == 'F':
            ni, nj = ci+delta[d][0], cj+delta[d][1]
            if d == 0 and mn_i > ni:
                mn_i = ni
            elif d == 1 and mx_j < nj:
                mx_j = nj
            elif d == 2 and mx_i < ni:
                mx_i = ni
            elif d == 3 and mn_j > nj:
                mn_j = nj
            ci, cj = ni, nj
        elif order == 'B':
            ni, nj = ci-delta[d][0], cj-delta[d][1]
            if d == 0 and mx_i < ni:
                mx_i = ni
            elif d == 1 and mn_j > nj:
                mn_j = nj
            elif d == 2 and mn_i > ni:
                mn_i = ni
            elif d == 3 and mx_j < nj:
                mx_j = nj
            ci, cj = ni, nj
        elif order == 'L':
            d = (d-1) % 4
        else:
            d = (d+1) % 4

    print(abs(mx_i-mn_i) * abs(mx_j-mn_j))