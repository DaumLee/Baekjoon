from collections import deque


def adventure(si, sj):
    q = deque([(si, sj)])
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        if 97 <= ord(arr[ci][cj]) <= 122:
            query.append((v[ci][cj]-1, arr[ci][cj]))
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and arr[ni][nj] != 'X':
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))


N, M, P = map(int, input().split())
arr = []
loc = dict()
for i in range(N):
    lst = list(input())
    for j in range(M):
        if lst[j] == 'B':
            ei, ej = i, j
        elif 97 <= ord(lst[j]) <= 122:
            loc[lst[j]] = (i, j)
    arr.append(lst)

ad = dict()
for _ in range(P):
    id, dps = input().split()
    ad[id] = int(dps)

HP = int(input())

query = []
adventure(ei, ej)
query.sort()

now = -1
arrived = []
for q in query:
    time, id = q
    if now == -1: now = time
    if now != time:
        for player in arrived:
            HP -= ad[player]*(time-now)
    if HP <= 0:
        break
    arrived.append(id)
    now = time
print(len(arrived))