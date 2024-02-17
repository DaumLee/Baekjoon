def check(board):
    cnt = 0
    # 케이스 하나 가정
    line = ['W', 'B'] * 4

    for k in range(len(board)):
        if line == board[k]:
            line = line[::-1]
        else:
            for l in range(len(board[k])):
                if board[k][l] != line[l]:
                    cnt += 1
            line = line[::-1]

    # WB 보다 BW 케이스가 더 빠른 경우 64-cnt로 리턴
    return min(cnt, 64 - cnt)

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

mn = 64

for i in range(N-7):
    for j in range(M-7):
        board = [a[j:j+8] for a in arr[i:i+8]]
        mn = min(check(board), mn)

print(mn)