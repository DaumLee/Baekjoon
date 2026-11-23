def _2048(board, d):
    # 이동 결과를 담을 새 보드와 최댓값
    nxt = [[0] * N for _ in range(N)]
    val = 0
    # 밀리는 방향의 반대로 ㄱㄱ
    di, dj = delta[(d+2)%4]

    for k in range(N):
        # 방향별 시작 좌표 설정
        if d == 0:
            si, sj = 0, k
        elif d == 1:
            si, sj = k, N-1
        elif d == 2:
            si, sj = N-1, k
        else:
            si, sj = k, 0

        ci, cj = si, sj
        ni, nj = si, sj
        prev = 0

        for _ in range(N):
            x = board[ci][cj]
            if x:
                # 대기 중인 블록이 없으면 현재 블록 보관
                if prev == 0:
                    prev = x
                # 같은 블록이면 합치고 초기화
                elif prev == x:
                    nv = prev * 2
                    nxt[ni][nj] = nv
                    if nv > val: val = nv
                    ni += di
                    nj += dj
                    prev = 0
                # 다른 블록이면 이전 블록 위치 고정하고 현재 블록 보관
                else:
                    nxt[ni][nj] = prev
                    if prev > val: val = prev
                    ni += di
                    nj += dj
                    prev = x
            ci += di
            cj += dj

        # 마지막 남은 블록
        if prev:
            nxt[ni][nj] = prev
            if prev > val: val = prev

    return nxt, val


def dfs(n, board, val):
    global mx

    if val > mx:
        mx = val
    if n == 10:
        return
    # 가지치기
    if val * (2 ** (10 - n)) <= mx:
        return

    for d in range(4):
        nxt, nval = _2048(board, d)
        if nxt != board:
            dfs(n+1, nxt, nval)


N = int(input())
arr = []
# 점수
mx = 0
for i in range(N):
    lst = list(map(int, input().split()))
    for x in lst:
        if x > mx:
            mx = x
    arr.append(lst)

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
dfs(0, arr, mx)
print(mx)