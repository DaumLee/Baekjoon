# 시작점
start = input()
prev = start
# 정답 처리 분기
flag = 1
# 체스판 방문 확인
board = [[0] * 6 for _ in range(6)]
board[ord(prev[0])-65][int(prev[1])-1] = 1

# 시작점 제외하고 35번 반복하면서
for i in range(35):
    # 다음으로 갈 칸
    next = input()
    # 인덱스로 변환
    ni, nj = ord(next[0]) - 65, int(next[1]) - 1

    # 나이트의 이동 반경에 해당하면
    if abs(ord(next[0])-ord(prev[0])) == 2 and abs(int(next[1])-int(prev[1])) == 1:
        board[ni][nj] = 1
    elif abs(ord(next[0])-ord(prev[0])) == 1 and abs(int(next[1])-int(prev[1])) == 2:
        board[ni][nj] = 1
    # 나이트가 이동할 수 없으면 break
    else:
        flag = 0
        break

    prev = next

# 시작점으로 돌아올 수 없으면
if not ((abs(ord(next[0]) - ord(start[0])) == 2 and abs(int(next[1]) - int(start[1])) == 1) or (abs(ord(next[0]) - ord(start[0])) == 1 and abs(int(next[1]) - int(start[1])) == 2)):
    flag = 0

if flag:
    sm = 0
    for i in range(6):
        sm += sum(board[i])
    if sm != 36:
        flag = 0

if flag:
    print('Valid')
else:
    print('Invalid')