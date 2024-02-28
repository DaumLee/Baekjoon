def magician(si, sj):
    global ans
    shape = tet[4]
    for t in shape:
        # 지금 도형을 뒀을 때의 합계
        sm = board[si][sj]
        # 4칸을 만들러 이동
        for di, dj in t:
            ni, nj = si+di, sj+dj
            # 범위를 한번이라도 벗어나면 해당 테트로미노를 둘 수 없음
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                break
            sm += board[ni][nj]
        # 매 시도마다 최댓값 갱신
        ans = max(ans, sm)


# 테트로미노 하나를 정해서 합계를 구함
def solve(si, sj, k):
    global ans
    # 모양
    shape = tet[k]
    for t in shape:
        # 지금 도형을 뒀을 때의 합계
        sm = board[si][sj]
        ci, cj = si, sj
        # 4칸을 만들러 이동
        for di, dj in t:
            ni, nj = ci+di, cj+dj
            # 범위를 한번이라도 벗어나면 해당 테트로미노를 둘 수 없음
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                break
            sm += board[ni][nj]
            # 다음 칸으로 이동하면서 테트로미노 모양 맞춰감
            ci, cj = ni, nj
        # 매 시도마다 최댓값 갱신
        ans = max(ans, sm)


N, M = map(int, input().split())
tet = [[((0, 1), (0, 1), (0, 1)), ((1, 0), (1, 0), (1, 0))],
       [((0, 1), (1, 0), (0, -1))],
       [((1, 0), (1, 0), (0, 1)), ((0, 1), (1, 0), (1, 0)), ((1, 0), (0, 1), (0, 1)), ((1, 0), (0, -1), (0, -1)),
        ((0, -1), (0, -1), (1, 0)), ((0, 1), (0, 1), (1, 0)), ((0, -1), (1, 0), (1, 0)), ((1, 0), (1, 0), (0, -1))],
       [((1, 0), (0, 1), (1, 0)), ((1, 0), (0, -1), (1, 0)), ((0, 1), (1, 0), (0, 1)), ((0, -1), (1, 0), (0, -1))],
       [((0, -1), (-1, 0), (0, 1)), ((0, -1), (1, 0), (0, 1)), ((-1, 0), (0, -1), (1, 0)), ((-1, 0), (0, 1), (1, 0))]]

board = [list(map(int, input().split())) for _ in range(N)]
# 최댓값
ans = 0

for i in range(N):
    for j in range(M):
        for k in range(4):
            solve(i, j, k)
        magician(i, j)

print(ans)