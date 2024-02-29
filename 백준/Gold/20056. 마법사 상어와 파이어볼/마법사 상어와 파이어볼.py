from collections import deque

'''
초기에 표기를 올림으로 판단
--> 질량이 0이 될 수 있어야 하기 때문에 내림으로 판단
--> __floor__ 대신 int로 내림을 할 수 있음
'''


def move(s):
    # 질량 합, 속력 합, 개수, 방향 홀짝 체크
    v = [[[0, 0, 0, 0] for x in range(N)] for y in range(N)]
    for cur in s:
        # 차례대로 행, 열, 질량, 속력, 방향
        ci, cj, cm, cs, cd = cur
        # 이동 델타 값을 받은 후
        di, dj = delta[cd]
        # 속력만큼 이동, 행과 열은 연속함
        ni, nj = (ci+di*cs)%N, (cj+dj*cs)%N
        # 질량 더하고
        v[ni][nj][0] += cm
        # 속력 더하고
        v[ni][nj][1] += cs
        # 개수 +1
        v[ni][nj][2] += 1
        # 이번에 처음 들어온 거면 방향 입력
        if v[ni][nj][2] == 1:
            v[ni][nj][3] = cd
        # 지금까지 방향의 홀짝이 같았으나 이제 달라졌으면 -1로 변경
        elif v[ni][nj][3] != -1 and v[ni][nj][3]%2 != cd%2:
            v[ni][nj][3] = -1

    # 이동이 완료된 후 파이어볼의 정보 저장
    nxt = []
    # v 순회
    for i in range(N):
        for j in range(N):
            # 값이 하나라도 들어왔으면
            if sum(v[i][j]) or v[i][j][3] == -1:
                # 하나 들어왔으면
                if v[i][j][2] == 1:
                    nxt.append((i, j, v[i][j][0], v[i][j][1], v[i][j][3]))
                else:
                    m, s = int(v[i][j][0]/5), int(v[i][j][1]/v[i][j][2])
                    # 4번 케이스를 만나면
                    if m == 0:
                        continue
                    # 방향이 다르면
                    if v[i][j][3] == -1:
                        nxt.append((i, j, m, s, 1))
                        nxt.append((i, j, m, s, 3))
                        nxt.append((i, j, m, s, 5))
                        nxt.append((i, j, m, s, 7))
                    # 방향이 모두 같으면
                    else:
                        nxt.append((i, j, m, s, 0))
                        nxt.append((i, j, m, s, 2))
                        nxt.append((i, j, m, s, 4))
                        nxt.append((i, j, m, s, 6))

    # 이동이 완료된 파이어볼의 위치를 리턴
    return nxt


N, M, K = map(int, input().split())
# 8방 이동 델타
delta = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

# 초기 파이어볼 정보 저장
fb = []
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fb.append((r-1, c-1, m, s, d))

# 파이어볼의 정보 k번 최신화
for i in range(K):
    fb = move(fb)

# 파이어볼 정보 최신화가 끝났으면
sm = 0
for f in fb:
    # 모든 질량을 더함
    sm += f[2]

print(sm)