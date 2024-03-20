from collections import deque

def count(si, sj):
    q = deque([(si, sj)])
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and arr[ni][nj] == arr[si][sj]:
                q.append((ni, nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
dice = [1, 2, 3, 4, 5, 6]
# 주사위 회전
move_dice = {
    0: {0: 4, 1: 0, 2: 2, 3: 3, 4: 5, 5: 1},
    1: {0: 3, 1: 1, 2: 0, 3: 5, 4: 4, 5: 2},
    2: {0: 1, 1: 5, 2: 2, 3: 3, 4: 0, 5: 4},
    3: {0: 2, 1: 1, 2: 5, 3: 0, 4: 4, 5: 3}
}
ci = 0
cj = 0
# 최초 오른쪽으로 이동
cd = 1
# 점수
sm = 0
for _ in range(K):
    # 주사위 좌표 이동
    di, dj = delta[cd]
    ni, nj = ci+di, cj+dj
    # 못가면 방향 반대
    if not (0 <= ni < N and 0 <= nj < M):
        cd = (cd+2)%4
        di, dj = delta[cd]
    ci, cj = ci+di, cj+dj
    new_dice = [0] * 6
    # 주사위 번호 이동
    for num in range(6):
        new_dice[num] = dice[move_dice[cd][num]]
    # 점수 획득
    sm += count(ci, cj)*arr[ci][cj]
    # 방향 변경
    if new_dice[-1] > arr[ci][cj]:
        cd = (cd+1)%4
    if new_dice[-1] < arr[ci][cj]:
        cd = (cd-1)%4
    dice = new_dice
print(sm)