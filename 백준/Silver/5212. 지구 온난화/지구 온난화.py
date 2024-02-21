def check(ci, cj):
    cnt = 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci+di, cj+dj
        # 바다 체크
        if 0 <= ni < len(graph) and 0 <= nj < len(graph[0]) and graph[ni][nj] == '.':
            cnt += 1
    if cnt >= 3:
        return True
    return False


N, M = map(int, input().split())
graph = []
land = []
for i in range(N):
    lst = input()
    graph.append('.'+lst+'.')

graph = ['.' * (M+2)] + graph + ['.' * (M+2)]
# print(graph)
# print(land)

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 'X':
            land.append((i, j))

ans = []
mx_i = mx_j = 0
mn_i, mn_j = N+1, M+1
# 하나씩 보냄
for ci, cj in land:
    # 가라 앉지 않는 땅만 저장
    if not check(ci, cj):
        ans.append((ci, cj))
        if ci > mx_i:
            mx_i = ci
        if cj > mx_j:
            mx_j = cj
        if ci < mn_i:
            mn_i = ci
        if cj < mn_j:
            mn_j = cj


# print(ans)
# print(mx_i, mn_i, mx_j, mn_j)

ret = [['.'] * (mx_j-mn_j+1) for _ in range(mx_i-mn_i+1)]

for i in range(0, mx_i-mn_i+1):
    for j in range(0, mx_j-mn_j+1):
        if (i+mn_i, j+mn_j) in ans:
            ret[i][j] = 'X'

for line in ret:
    print(''.join(line))