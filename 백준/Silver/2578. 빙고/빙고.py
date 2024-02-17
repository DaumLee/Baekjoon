def bingo(board):
    # 빙고 수 카운트
    cnt = 0

    # 가로열 확인
    for i in range(5):
        if sum(board[i]) == 5:
            cnt += 1
            if cnt == 3:
                return 1

    # 빙고판 돌리고 세로열 확인
    board_t = list(map(list, zip(*board)))
    for i in range(5):
        if sum(board_t[i]) == 5:
            cnt += 1
            if cnt == 3:
                return 1

    # \ 대각선 확인
    sm = 0
    for j in range(5):
        if board[j][j]:
            sm += 1
        if sm == 5:
            cnt += 1
            if cnt == 3:
                return 1

    # / 대각선 확인
    sm = 0
    for j in range(5):
        if board[4-j][j]:
            sm += 1
            if sm == 5:
                cnt += 1
                if cnt == 3:
                    return 1
    return 0

# 번호 빙고판
arr = [list(map(int, input().split())) for _ in range(5)]
# 부를 숫자 리스트
ans = list()
# 숫자가 불리면 해당 칸을 1로 채움
board = [[0] * 5 for _ in range(5)]
# 반복문 분기를 위해..flag 설정
flag = 1

# 사회자가 부르는 수를 1차원 배열로 받음
for _ in range(5):
    ans += map(int, input().split())

for i in range(25):
    # 빙고가 완성되면 하부 코드를 실행하지 않음
    if flag:
        # 부르는 숫자
        call = ans[0]
        for a in range(5):
            if flag:
                for b in range(5):
                    # 숫자가 불리면 해당 칸에 1로 체크
                    if call == arr[a][b] and flag:
                        board[a][b] = 1
                        # 부른 정답 제거
                        ans.pop(0)
                        if bingo(board):
                            # 숫자 출력 후 반복문 탈출
                            print(i+1)
                            flag = 0