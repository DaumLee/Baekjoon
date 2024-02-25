def check(ci, cj):
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci+di, cj+dj
        # 늑대 바로 옆에 양이 있으면 0 출력하고 종료
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 'S':
            print(0)
            exit(0)


N, M = map(int, input().split())
board = []
wolf = []
for i in range(N):
    lst = list(input())
    board.append(lst)
    for j in range(M):
        if lst[j] == 'W':
            wolf.append((i, j))

# 늑대 바로 옆에 양이 있는지 확인
for w in wolf:
    check(*w)

print(1)
# 최소 개수가 아니니 싹다 울타리로 표시
for i in range(N):
    for j in range(M):
        print(board[i][j] if board[i][j] != '.' else 'D', end='')
    print()