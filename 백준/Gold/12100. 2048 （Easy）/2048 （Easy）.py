from collections import deque

def _2048(dirs, cnt):
    board = [lst[:] for lst in arr]
    q = deque()
    for d in dirs:
        di, dj = delta[d]
        # 합쳐진 상태를 표시
        v = [[0] * N for _ in range(N)]
        if d == 0 or d == 3:
            for i in range(N):
                for j in range(N):
                    if board[i][j]:
                        q.append((i, j))
        else:
            for i in range(N-1, -1, -1):
                for j in range(N-1, -1, -1):
                    if board[i][j]:
                        q.append((i, j))
        while q:
            ci, cj = q.popleft()
            # 블록이 하나 남았으면 종료
            if cnt == 1:
                return board[ci][cj]
            while True:
                ni, nj = ci+di, cj+dj
                if 0 <= ni < N and 0 <= nj < N:
                    # 블록을 만났는데
                    if board[ni][nj]:
                        # 같은 블록을 만나면 내 값을 지우고 다음 값을 *2해서 종료
                        # 추가 : 다음 블록이나 현재 블록이 지금 이동에서 이미 합쳐진 상태가 아닐 경우만 합침
                        if board[ni][nj] == board[ci][cj] and not v[ni][nj] and not v[ci][cj]:
                            board[ni][nj] *= 2
                            board[ci][cj] = 0
                            # 지금 블록은 사라지니까 다음 블록만 합침 처리
                            v[ni][nj] = 1
                            cnt -= 1
                        # 다른 블록이면 합칠 수 없어 이동할 수 없고 바로 종료
                        break
                    # 블록을 만나지 못했다면 계속 전진
                    else:
                        board[ni][nj] = board[ci][cj]
                        board[ci][cj] = 0
                        # 합친 여부를 다음 칸으로 전달
                        v[ni][nj] = v[ci][cj]
                        v[ci][cj] = 0
                        ci, cj = ni, nj
                # 범위 바깥으로 나갈 수는 없으니 이동하지 못하고 종료
                else:
                    break
    val = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > val:
                val = board[i][j]

    return val


def permutations(n, dirs, cnt):
    global mx

    if n == 5:
        score = _2048(dirs, cnt)
        mx = max(mx, score)
        return

    for i in range(4):
        permutations(n+1, dirs+[i], cnt)


N = int(input())
arr = []
# 블록의 전체 개수
block = 0
# 점수
mx = 0
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j]:
            block += 1
    arr.append(lst)

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
permutations(0, [], block)
print(mx)