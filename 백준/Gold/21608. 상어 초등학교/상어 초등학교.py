def find_blank(ci, cj):
    cnt = 0
    for di, dj in delta:
        ni, nj = ci+di, cj+dj
        # 비어있는 칸 카운트
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == -1:
            cnt += 1

    return cnt


def fix(n, lst):
    v = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 좋아하는 학생이면
            if arr[i][j] in lst:
                for di, dj in delta:
                    ni, nj = i+di, j+dj
                    # 앉을 수 있는 칸만 인접 체크
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == -1:
                        v[ni][nj] += 1

    # 자리 후보
    cand = []
    # 인접 최댓값
    mx = -1
    for i in range(N):
        for j in range(N):
            # 이미 좌석이 있는 칸이라면 pass
            if arr[i][j] != -1:
                continue
            # 인접 빈칸이 현재까지의 최댓값보다 크다면 초기화
            if v[i][j] > mx:
                mx = v[i][j]
                cand = [(i, j)]
            # 인접 빈칸 수가 최댓값과 같다면 append
            elif v[i][j] == mx:
                cand.append((i, j))

    # 혹시 모르니까
    seat = cand[0]
    # 빈칸 최댓값
    b = -1
    # 빈칸 확인
    for ci, cj in cand:
        cnt = find_blank(ci, cj)
        # 더 많은 빈칸 발견
        if b < cnt:
            b = cnt
            seat = (ci, cj)

    # 최종 좌석 결정
    arr[seat[0]][seat[1]] = n


N = int(input())
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
like = dict()
# 최종 좌석 배치
arr = [[-1] * N for _ in range(N)]

# 배치 순서
seq = []

for i in range(N**2):
    n, a, b, c, d = map(int, input().split())
    like[n-1] = [a-1, b-1, c-1, d-1]
    seq.append(n-1)

for i in seq:
    n, lst = i, like[i]
    # 처음 배치는 무조건 (1, 1)
    if i == seq[0]:
        arr[1][1] = n
    else:
        fix(n, lst)

score = 0
for i in range(N):
    for j in range(N):
        student = arr[i][j]
        cnt = 0
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                for item in like[student]:
                    if arr[ni][nj] == item:
                        cnt += 1

        if cnt == 1:
            score += 1
        elif cnt == 2:
            score += 10
        elif cnt == 3:
            score += 100
        elif cnt == 4:
            score += 1000

print(score)