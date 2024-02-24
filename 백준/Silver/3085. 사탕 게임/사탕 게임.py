def play():
    global ans

    # 해당 시행에서의 최대 연속 길이(최소는 연속이 없는 상태인 1)
    mx = 1
    # axis = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            # 연속이면
            if board[i][j] == board[i][j-1]:
                cnt += 1
            # 연속이 아니면
            else:
                cnt = 1
            mx = max(mx, cnt)

    # axis = 0
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            # 연속이면
            if board[i][j] == board[i-1][j]:
                cnt += 1
            # 연속이 아니면
            else:
                cnt = 1
            mx = max(mx, cnt)
    # 최댓값 갱신
    ans = max(ans, mx)


N = int(input())
board = [list(input()) for _ in range(N)]
ans = 1

# 교환
for i in range(N):
    for j in range(N):
        # 오른쪽과 다르면 교환
        if j < N-1 and board[i][j] != board[i][j+1]:
            # 오른쪽과 교환
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            play()
            # 원복
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        # 아래와 다르면 교환
        if i < N-1 and board[i][j] != board[i+1][j]:
            # 아래와 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            play()
            # 원복
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)