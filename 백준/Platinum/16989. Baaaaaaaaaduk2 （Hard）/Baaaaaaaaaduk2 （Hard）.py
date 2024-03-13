from collections import deque, defaultdict

# 2는 상대의 돌
# 1은 내 돌
# 0은 빈칸

BLANK, ME, ENEMY = 0, 1, 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    # bfs에서 가져와야 하는 것 - 놓아야 죽는 좌표, 죽으면 몇개의 돌이 죽는지의 밸류
    q = deque()
    visited[i][j] = 1
    q.append((i, j))
    cnt = 1
    coors = set()
    flag = True

    while q:
        x, y = q.popleft()
        for d in range(len(dx)):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if flag and board[nx][ny] == BLANK:
                    # 아직 글러먹지않았고, 옆이 열린 칸이면 coors 반영
                    coors.add((nx, ny))
                elif board[nx][ny] == ENEMY:
                    # 옆도 적 돌이면 q 어펜드, cnt 반영
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
                # 옆이 막힌 칸이면 그냥 두기
        if len(coors) >= 3:
            # 가능하지 않으면 플래그 펄스
            flag = False

    # 가능한 경우에는
    if flag:
        return True, coors, cnt
    else:
        return False, -1, -1


h, w = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
# bfs에서 가져와야 하는 것 - 놓아야 죽는 좌표, 죽으면 몇개의 돌이 죽는지의 밸류
candidates = defaultdict(int)

for i in range(h):
    for j in range(w):
        if board[i][j] == ENEMY and not visited[i][j]:
            is_possible, coors, cnt = bfs(i, j)
            if is_possible:
                candidates[tuple(sorted(tuple((coors))))] += cnt

one_list = []
one_additional = defaultdict(int)
two_list = []

for k, v in candidates.items():
    if len(k) == 2:
        two_list.append((v, k))
        # k의 특정 좌표에서 하나만 더 두면 가져갈 수 있는 추가득점. 하지만 이건 더하면 안되고, 택1이다.
        one_additional[k[0]] = max(one_additional[k[0]], v)
        one_additional[k[1]] = max(one_additional[k[1]], v)
    else:
        one_list.append((v, k))

one_list.sort(reverse=True)
two_list.sort(reverse=True)

# 1칸짜리 두개
sm1, sm2, sm3 = 0, 0, 0

if len(one_list) == 0:  # 1칸짜리가 없다면
    sm1 = 0

else:  # 1칸짜리 최소 하나 이상
    if len(one_list[0][1]) == 1:
        sm2 = one_list[0][0] + one_additional[one_list[0][1][0]]

    if len(one_list) >= 2:
        sm1 = one_list[0][0] + one_list[1][0]
    else:
        sm1 = one_list[0][0]

# 두칸짜리 큰거 하나
if two_list:
    sm3 = two_list[0][0]

answer = max(sm1, sm2, sm3)

print(answer)
