from collections import deque


def move(si, sj, d):
    # 방향을 저장
    v = [[-1] * N for _ in range(N)]
    # 최초 꼬리 위치
    ti, tj = si, sj
    # 최초 머리 위치
    hi, hj = si, sj
    # 시작 방향은 오른쪽
    v[0][0] = 0
    t = 0
    while True:
        t += 1
        # 딱 한칸 전진
        di, dj = delta[d]
        # 다음 머리 위치
        ni, nj = hi+di, hj+dj
        # 범위 내에서
        if 0 <= ni < N and 0 <= nj < N:
            # 머리가 이동했을 때 몸과 부딪히면 종료
            if v[ni][nj] != -1:
                return t
            # 갈 수 있으면 현재 위치에 이동 방향을 저장(인덱스 에러 수정)하고 전진
            v[hi][hj] = d
            hi, hj = ni, nj
            for a in range(len(apple)):
                # 사과가 있으면
                if apple[a][0] == ni and apple[a][1] == nj and not v_apple[a]:
                    v_apple[a] = 1
                    break
            # 사과가 없으면 꼬리가 한칸 전진하고 해당 칸 미방문으로 변경
            else:
                td = v[ti][tj]
                v[ti][tj] = -1
                ti, tj = ti+delta[td][0], tj+delta[td][1]

        # 범위를 벗어나면 종료
        else:
            return t

        # 방향을 바꿀 시간이면
        if time and t == time[0]:
            if turn[0] == 'L':
                d = (d-1)%4
            else:
                d = (d+1)%4
            time.popleft()
            turn.popleft()


N = int(input())
K = int(input())
apple = []
for _ in range(K):
    i, j = map(int, input().split())
    apple.append((i-1, j-1))
# 사과 방문 여부
v_apple = [0] * len(apple)
L = int(input())
# 방향을 바꾸는 시간
time = deque()
# 회전하는 방향
turn = deque()
for _ in range(L):
    t, d = input().split()
    time.append(int(t))
    turn.append(d)

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

print(move(0, 0, 0))