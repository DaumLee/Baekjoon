def curve(item):
    ci, cj, sd, g = item
    pre = []
    for i in range(g+1):
        # 0세대 작성
        if i == 0:
            arr[ci][cj] = 1
            ni, nj = ci+delta[sd][0], cj+delta[sd][1]
            arr[ni][nj] = 1
            ci, cj = ni, nj
            pre.append(sd)
        # 1세대 작성
        elif i == 1:
            arr[ci][cj] = 1
            ni, nj = ci + delta[(sd+1)%4][0], cj + delta[(sd+1)%4][1]
            arr[ni][nj] = 1
            ci, cj = ni, nj
            pre.append((sd+1)%4)
        # 2세대 이상 작성
        else:
            for d in range(len(pre)):
                # 직전 세대 선분이 아니면 180도 회전 진행
                if d < 2**(i-2):
                    nd = (pre[d]+2)%4
                # 직전 세대 선분은 방향 그대로 진행
                else:
                    nd = pre[d]
                ni, nj = ci+delta[nd][0], cj+delta[nd][1]
                arr[ni][nj] = 1
                pre.append(nd)
                ci, cj = ni, nj


N = int(input())
arr = [[0] * 101 for _ in range(101)]
delta = ((0, 1), (-1, 0), (0, -1), (1, 0))

lst = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    lst.append((y, x, d, g))

for item in lst:
    curve(item)

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            cnt += 1

print(cnt)