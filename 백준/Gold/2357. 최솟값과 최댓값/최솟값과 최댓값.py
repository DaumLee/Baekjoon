def seg_tree(n, l, r):
    # 딱 요소 하나의 값만 저장한 상태에서 해당 요소의 값 리턴
    if l == r:
        sgt[n] = (lst[l], lst[l])
        return sgt[n]
    
    m = (l+r) // 2
    sm_l = seg_tree(2*n, l, m)
    sm_r = seg_tree(2*n+1, m+1, r)
    # 최솟값 / 최댓값 순으로 저장
    sgt[n] = (min(sm_l[0], sm_r[0]), max(sm_l[1], sm_r[1]))
    return sgt[n]


def solve(n, l, r, a, b):
    # 값을 갱신할 수 없도록 최솟값과 최댓값을 반대로 넣음
    if b < l or r < a:
        return 10e8, 0
    if r <= b and a <= l:
        return sgt[n]

    m = (l+r) // 2
    sm_l = solve(n*2, l, m, a, b)
    sm_r = solve(n*2+1, m+1, r, a, b)
    return min(sm_l[0], sm_r[0]), max(sm_l[1], sm_r[1])


N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]

# 세그먼트 트리(포화 이진트리로 작성)
sgt = [0 for _ in range(N*4)]
seg_tree(1, 0, N-1)

for _ in range(M):
    a, b = map(int, input().split())
    print(*solve(1, 0, N-1, a-1, b-1))