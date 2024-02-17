import sys
input = sys.stdin.readline


def solve(si, sj, size):
    global idx, ans

    # 지금 2x2칸에 r, c가 존재, idx 계산해서 정답 갱신
    if size == 2:
        ans = idx + 2*(r-si) + (c-sj)
        return

    if size > 2:
        # 2사분면만 계산
        if r < si+size//2 and c < sj+size//2:
            solve(si, sj, size//2)
        # 1사분면만 계산, 2사분면 순번 더함
        elif r < si+size//2:
            idx += (size//2)**2
            solve(si, sj+size//2, size//2)
        # 3사분면만 계산, 2~1사분면 순번 더함
        elif c < sj+size//2:
            idx += 2*(size//2)**2
            solve(si+size//2, sj, size//2)
        # 4사분면만 계산, 2~1~3사분면 순번 더함
        else:
            idx += 3*(size//2)**2
            solve(si+size//2, sj+size//2, size//2)


N, r, c = map(int, input().split())
idx = 0
ans = 0
solve(0, 0, 2**N)
print(ans)