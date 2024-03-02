def check(h):
    global time, height

    # 채울 블록 개수
    fill = 0
    # 제거할 블록 개수
    rmve = 0

    for i in range(N):
        for j in range(M):
            # 높이 보다 작다면 블록을 채워야 함
            if h > board[i][j]:
                # 필요한 블록의 수
                fill += h-board[i][j]
            # 높이 보다 크면 블록을 제거해야 함
            elif h < board[i][j]:
                rmve += board[i][j]-h

    # 채울 수 없으면 넘어감
    if fill > B+rmve:
        return
    # 현재 단계에서 걸리는 시간이 최소면 정답 갱신, 낮은 높이부터 탐색하기 때문에 = 조건 추가
    if fill + rmve*2 <= time:
        time = fill + rmve*2
        height = h


N, M, B = map(int, input().split())
board = []
mx = 0

for i in range(N):
    lst = list(map(int, input().split()))
    board.append(lst)
    mx = max(mx, max(lst))

time = 6.4*10e7
height = 0

for h in range(0, mx+1):
    check(h)

print(time, height)