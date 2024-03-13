def seg_tree(n, l, r):
    # 딱 요소 하나의 값만 저장한 상태에서 해당 요소의 값 리턴
    if l == r:
        sgt[n] = lst[l]
        return sgt[n]
    
    m = (l+r) // 2
    sm_l = seg_tree(2*n, l, m)
    sm_r = seg_tree(2*n+1, m+1, r)
    # 자식 두개의 값이 정해졌으면 곱해서 저장 / 시간초과 방지를 위해 모듈러 연산 추가
    sgt[n] = (sm_l * sm_r) % 1000000007
    return sgt[n]


# 주의 : b < c
def solve(n, l, r, b, c):
    if c < l or r < b:
        return 1
    if r <= c and b <= l:
        return sgt[n]

    m = (l+r) // 2
    sm_l = solve(n*2, l, m, b, c)
    sm_r = solve(n*2+1, m+1, r, b, c)
    return (sm_l * sm_r) % 1000000007


def update(n, l, r, b, c):
    if b < l or r < b:
        return
    if l == r == b:
        sgt[n] = c
        return

    m = (l+r) // 2
    update(n*2, l, m, b, c)
    update(n*2+1, m+1, r, b, c)
    # 자식들 값 변경이 끝나면 내 값 변경하고 종료
    sgt[n] = (sgt[n*2] * sgt[n*2+1]) % 1000000007


N, M, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

# 세그먼트 트리(포화 이진트리로 작성)
sgt = [0 for _ in range(N*4)]
seg_tree(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(solve(1, 0, N-1, b-1, c-1))