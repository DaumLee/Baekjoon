'''
가속은 곧 힘
힘은 곧 가속도 되니
F = ma
force = mass * acceleration
'''

def catch(j):
    for i in range(N):
        if arr[i][j]:
            ret = arr[i][j][2]
            arr[i][j] = 0
            return ret
    return 0

def move():
    new = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 상어가 없는 칸은 처리하지 않음
            if not arr[i][j]: continue
            s, d, z = arr[i][j]
            # 열 이동
            if d >= 3:
                # 일단 다 더해놓고
                ni, nj = i, j + s * delta[d][1]
                e, m = divmod(nj, M-1)
                # 원 방향대로 가면
                if e % 2 == 0: nj = m
                # 방향을 바꾸는 경우
                else: d = turn[d]; nj = (M-1)-m
            # 행 이동
            else:
                ni, nj = i + s * delta[d][0], j
                e, m = divmod(ni, N-1)
                # 원 방향대로 가면
                if e % 2 == 0: ni = m
                # 방향을 바꾸는 경우
                else: d = turn[d]; ni = (N-1)-m
            if not new[ni][nj] or new[ni][nj][2] < z: new[ni][nj] = (s, d, z)
    return new

N, M, K = map(int, input().split())
delta = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}
turn = {1: 2, 2: 1, 3: 4, 4: 3}
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    si, sj, s, d, z = map(int, input().split())
    arr[si-1][sj-1] = (s, d, z)

ans = 0
for j in range(M):
    ans += catch(j)
    arr = move()

print(ans)