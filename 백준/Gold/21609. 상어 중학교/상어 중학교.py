from collections import deque, defaultdict

def gravity():
    # 행 확인
    for i in range(N-2, -1, -1):
        for j in range(N):
            ci = i
            # 흰 블록이랑 색 블록만 이동
            if arr[i][j] >= 0:
                while True:
                    ni = ci+1
                    if ni >= N:
                        break
                    # 빈칸으로만 내려갈 수 있음
                    if arr[ni][j] == -2:
                        ci = ni
                    else:
                        break
                arr[i][j], arr[ci][j] = -2, arr[i][j]


def scoring(si, sj):
    # 색
    c = arr[si][sj]
    q = deque([(si, sj)])
    v[si][sj] = c
    arr[si][sj] = -2
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            # 흰 블록이거나 지금이랑 같은 색인 경우만 그룹 가능
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] != c and (not arr[ni][nj] or arr[ni][nj] == c):
                # 맵에서 삭제
                arr[ni][nj] = -2
                v[ni][nj] = c
                q.append((ni, nj))


def grouping(si, sj):
    global mx, groups, mx_blocks
    # 색
    c = arr[si][sj]
    q = deque([(si, sj)])
    v[si][sj] = c
    # 기준 블록
    ei, ej = si, sj
    # 무지개 블록 수
    cnt = 0
    # 전체 블록 수
    blocks = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            # 흰 블록이거나 지금이랑 같은 색인 경우만 그룹 가능, 흰 블록은 계속 먹을 수 있으니 방문은 현재 색으로 표시, 비교 (11시)
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] != c and (not arr[ni][nj] or arr[ni][nj] == c):
                # 일반 블록일 경우 기준 블록 갱신 체크
                if arr[ni][nj]:
                    if ni < si:
                        ei, ej = ni, nj
                    elif ni == si and nj < sj:
                        ei, ej = ni, nj
                else:
                    cnt += 1
                q.append((ni, nj))
                v[ni][nj] = c
                blocks += 1
    if blocks >= 2:
        groups += 1
        # 무지개 블록이 cnt인 경우 기준 블록 추가
        dct[blocks].append((cnt, ei, ej))
        mx_blocks = max(mx_blocks, blocks)
        if cnt > mx:
            mx = cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 시작
while True:
    dct = defaultdict(list)
    v = [[0] * N for _ in range(N)]
    # 최대 무지개 블록 개수
    mx = 0
    # 생성된 그룹 개수
    groups = 0
    # 최대 블록 개수
    mx_blocks = 0
    # 모든 경우의 수 그룹핑
    for i in range(N):
        for j in range(N):
            # 흰 블록, 검은 블록이 아니고, 집합에 포함되지 않았고, 빈 칸이 아닌 경우 그룹핑 시행
            if arr[i][j] and arr[i][j] != -1 and not v[i][j] and arr[i][j] != -2:
                grouping(i, j)
    # 그룹이 없는 경우 종료
    if not groups:
        break
    cand = []
    mx_rainbow = 0
    # 무지개 블록이 가장 많은 것들만 후보군에 넣음
    for cnt, mi, mj in dct[mx_blocks]:
        if cnt > mx_rainbow:
            # 최신화 추가 (10시 55분)
            mx_rainbow = cnt
            # 최댓값이 바뀌면 배열 초기화
            cand = [(mi, mj)]
        # 최댓값이 같으면 후보군으로 추가
        elif cnt == mx_rainbow:
            cand.append((mi, mj))
    ai = aj = 0
    # 후보군 탐색
    for i in range(len(cand)):
        if cand[i][0] > ai:
            ai, aj = cand[i][0], cand[i][1]
        elif cand[i][0] == ai and cand[i][1] > aj:
            ai, aj = cand[i][0], cand[i][1]
    # 점수 먹기
    v = [[0] * N for _ in range(N)]
    scoring(ai, aj)
    # 지우는 블록^2만큼 점수를 얻음
    ans += mx_blocks**2
    # 중력 작용
    gravity()
    # 반시계 회전
    arr = list(zip(*arr))[::-1]
    for line in range(len(arr)):
        arr[line] = list(arr[line])
    # 중력 작용
    gravity()
print(ans)