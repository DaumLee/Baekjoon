'''
최초 입력받은 맵, 방문 배열, 장애물 좌표 리스트를 불필요하게 전부 만들어서 통과
→ 장애물 좌표와 방문 배열을 합쳐 좌표를 모은 1차원 리스트로 만든 후 not in 비교 진행
 (O(n)이라 시간 초과)
→ 2차원 방문 배열 안에 장애물과 이동 경로를 모두 넣어 비교문을 O(1)로 변경 후 통과

다만 눈에 띄는 시간 차이나 메모리 차이는 없었습니다
'''

# 4방에 갈 수 있는 칸이 존재하는지 확인(이동 종료 조건)
def check(ci, cj):

    for di, dj in delta:
        ni, nj = ci+di, cj+dj
        # 내 위치에서 갈 수 있는 곳이 존재하면 종료하지 않음
        if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
            return True
    # 내 위치에서 갈 수 있는 곳이 없으면 종료함
    return False


def go(idx):
    global ci, cj, d

    ni, nj = ci+delta[idx][0], cj+delta[idx][1]
    # 장애물이 아니고, 범위 내에서 방문한 적이 없는 곳으로 갈 수 있으면 한 칸 전진
    if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
        v[ni][nj] = 1
        ci, cj = ni, nj
    # 못가면 다음 방향으로 변경
    else:
        d = (d+1) % 4


N, M = map(int, input().split())

# 장애물, 방문 좌표 모두 저장
v = [[0] * M for _ in range(N)]
for i in range(int(input())):
    ti, tj = map(int, input().split())
    v[ti][tj] = 1

# 시작점을 받아서 방문 처리
ci, cj = map(int, input().split())
v[ci][cj] = 1

# 오른쪽(4), 위(1), 아래(2), 왼쪽(3)
delta = ((0, 1), (-1, 0), (1, 0), (0, -1))
# 방향 인덱스 진행 순서
lst = list(map(int, input().split()))
d = 0

while check(ci, cj):
    # 방향 순서대로 넘겨줌
    go(lst[d] % 4)

print(ci, cj)