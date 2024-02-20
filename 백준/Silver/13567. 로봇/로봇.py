'''
오늘의 생활 상식
삼겹살은 사실 지방 + 살 + 지방의 세 겹으로 구성되어 있기 때문에
최빈값을 따졌을 때 삼겹지방이라고 부르는 것이 더 올바른 표기라고 생각합니다.
'''

def move(d):
    global idx, ci, cj, flag

    di, dj = delta[idx]
    # 계속해서 정해진 방향으로 전진
    for k in range(d):
        ni, nj = ci+di, cj+dj
        # 맵 내에서 이동할 수 있으면 이동
        if 0 <= ni < M and 0 <= nj < M:
            ci, cj = ni, nj
        # 이동할 수 없는 명령은 종료 후 더 이상 진행하지 않음
        else:
            flag = 0
            break


def turn(dir):
    global idx

    # dir이 1이면 왼쪽으로 회전
    if dir:
        idx = (idx-1) % 4
    # dir이 0이면 오른쪽으로 회전
    else:
        idx = (idx+1) % 4


M, n = map(int, input().split())
idx = 0
# 이동 방향(90도 회전)
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
ci = cj = 0
# 조건 분기
flag = 1
# 명령어 처리
for i in range(n):
    # 중간에 종료되지 않았다면
    if flag:
        o, d = input().split()
        if o == 'MOVE':
            move(int(d))
        else:
            turn(int(d))

# 중간에 종료했으면 -1을 출력
if flag:
    print(cj, ci)
else:
    print(-1)