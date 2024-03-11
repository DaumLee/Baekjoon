def charge(*lst):
    # 한 곳만 충전이 가능한 경우
    if len(lst) == 1:
        ci, cj = lst[0]
        # 최대 충전 충전기부터 찾아보면서
        for num, val in ap_desc:
            # 최대로 충전 가능한 충전기를 찾으면
            if num in arr[ci][cj]:
                # 바로 충전
                return ap[num]
    # 두 곳 모두 충전이 가능한 경우
    else:
        ai, aj = lst[0]
        bi, bj = lst[1]
        bc_a = []
        bc_b = []
        for num, val in ap_desc:
            if num in arr[ai][aj]:
                bc_a.append(num)
            if num in arr[bi][bj]:
                bc_b.append(num)
        # 최대 충전이 가능한 충전기가 다른 경우 그대로 충전
        if bc_a[0] != bc_b[0]:
            return ap[bc_a[0]]+ap[bc_b[0]]
        # 최대 충전이 가능한 충전기가 같은 경우 다른 충전기에 충전
        else:
            # 둘 다 백업 충전기가 있는 경우 둘 중 큰 값을 다른 충전기에서 충전
            if len(bc_a) >= 2 and len(bc_b) >= 2:
                if ap[bc_a[1]] > ap[bc_b[1]]:
                    return ap[bc_a[1]]+ap[bc_b[0]]
                else:
                    return ap[bc_a[0]]+ap[bc_b[1]]
            elif len(bc_a) >= 2:
                return ap[bc_a[1]] + ap[bc_b[0]]
            elif len(bc_b) >= 2:
                return ap[bc_a[0]] + ap[bc_b[1]]
            # 둘 다 백업 충전기가 없는 경우 균등 충전
            else:
                return ap[bc_a[0]]


delta = ((0, 0), (-1, 0), (0, 1), (1, 0), (0, -1))

for tc in range(1, int(input())+1):
    M, A = map(int, input().split())
    # 해당 칸에 위치한 발전기
    arr = [[list() for j in range(10)] for i in range(10)]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # power
    ap = dict()
    for k in range(A):
        apj, api, c, p = map(int, input().split())
        ap[k] = p
        for i in range(10):
            for j in range(10):
                if abs(api-i-1)+abs(apj-j-1) <= c:
                    arr[i][j].append(k)
    ap_desc = sorted(ap.items(), key=lambda x: -x[1])

    ai = aj = 0
    bi = bj = 9
    ans = 0
    for i in range(M+1):
        # 충전기가 모두 있을 때
        if arr[ai][aj] and arr[bi][bj]:
            ans += charge((ai, aj), (bi, bj))
        # A에만 충전기가 있을 때
        elif arr[ai][aj]:
            ans += charge((ai, aj))
        # B에만 충전기가 있을 때
        elif arr[bi][bj]:
            ans += charge((bi, bj))
        if i == M:
            break
        ai, aj = ai+delta[a[i]][0], aj+delta[a[i]][1]
        bi, bj = bi+delta[b[i]][0], bj+delta[b[i]][1]

    print(f'#{tc} {ans}')