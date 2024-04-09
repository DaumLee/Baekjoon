N, M = map(int, input().split())
ci, cj, d = map(int, input().split())
arr = [[1] * M for _ in range(N)]
v = [[[0] * 4 for _ in range(M)] for _ in range(N)]
rule = [[input() for _ in range(N)] for _ in range(2)]
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
dust = 0
time = 0
while True:
    time += 1
    flag = 1
    if arr[ci][cj]:
        arr[ci][cj] = 0
        dust += 1
        flag = 0
        ans = time
    else:
        if v[ci][cj][d] == dust: break
        v[ci][cj][d] = dust
    d = (d+int(rule[flag][ci][cj]))%4
    di, dj = delta[d]
    ci, cj = ci+di, cj+dj
    if not (0 <= ci < N and 0 <= cj < M): break
print(ans)