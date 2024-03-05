from collections import deque


def check(ai, aj, shape):
    cnt = 0
    # shape을 넣었을 때 갈 수 있는 칸
    can = []
    for di, dj in delta[shape]:
        ni, nj = ai+di, aj+dj
        can.append((ni, nj))

    # 정답의 4방과 상호 연결 상태를 확인
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ni, nj = ai+di, aj+dj
        # 갈 수 있는 칸이라면
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != '.':
            # z나 m은 길이 없으니 연결 상태만 확인
            if arr[ni][nj] == 'Z' or arr[ni][nj] == 'M':
                if (ni, nj) in can:
                    cnt += 1
                continue
            # 일단 탐색 시작
            for ndi, ndj in delta[arr[ni][nj]]:
                nni, nnj = ni+ndi, nj+ndj
                # 정답 칸과는 연결되어 있으나, 정답 칸에서는 연결되지 않은 칸을 찾은 경우
                if nni == ai and nnj == aj and (ni, nj) not in can:
                    return False
                elif nni == ai and nnj == aj:
                    cnt += 1

    # 모든 길이 제대로 연결되어 있으면 true
    if (shape == '+' and cnt < 4) or (shape != '+' and cnt < 2):
        return False
    return True


def bfs(si, sj, p):
    global ans, b
    q = deque(([(si, sj)]))

    while q:
        ci, cj = q.popleft()
        s = arr[ci][cj]
        for di, dj in delta[s]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and (not v[ni][nj] or ((ni, nj) in plus and v[ni][nj] < 2)) and (ni, nj) != p:
                if arr[ni][nj] == '.':
                    ans = [ni+1, nj+1]
                    for key, val in delta.items():
                        if key != 'M' and key != 'Z':
                            if check(ni, nj, key):
                                b = key
                                return
                if arr[ni][nj] == 'Z':
                    continue
                v[ni][nj] += 1
                q.append((ni, nj))


N, M = map(int, input().split())
arr = []
# +의 위치 저장
plus = []
for i in range(N):
    lst = list(input())
    arr.append(lst)
    for j in range(M):
        if lst[j] == 'M':
            si, sj = i, j
        elif lst[j] == 'Z':
            ei, ej = i, j
        elif lst[j] == '+':
            plus.append((i, j))

delta = {'.':(), 'M':((-1,0),(1,0),(0,1),(0,-1)), 'Z': ((-1,0),(1,0),(0,1),(0,-1)), '|': ((1, 0), (-1, 0)), '-': ((0, -1), (0, 1)), '+': ((1, 0), (-1, 0), (0, -1), (0, 1)),
         '1': ((0, 1), (1, 0)), '2': ((-1, 0), (0, 1)), '3': ((0, -1), (-1, 0)), '4': ((0, -1), (1, 0))}

v = [[0] * M for _ in range(N)]
v[si][sj] = 1
ans = [0, 0]
b = 0

for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
    ni, nj = si+di, sj+dj
    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != '.':
        # + 모양을 만났으면 encounter
        if (ni, nj) in plus:
            v[ni][nj] += 1
        # 모스크바의 다음 칸부터 dfs 시작
        bfs(ni, nj, (si, sj))
        break

print(*ans, b)