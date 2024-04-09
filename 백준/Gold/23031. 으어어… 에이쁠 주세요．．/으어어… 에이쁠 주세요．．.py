def switch(si, sj):
    light[si][sj] = 1
    for di, dj in l_delta:
        ni, nj = si+di, sj+dj
        if 0 <= ni < N and 0 <= nj < N:
            light[ni][nj] = 1


N = int(input())
A = input()
arr = []
zombie = []
loc = dict()
dr = dict()
num = 1
for i in range(N):
    lst = list(input())
    for j in range(N):
        if lst[j] == 'Z':
            zombie.append((i, j))
            loc[num] = (i, j)
            dr[num] = 0
            num += 1
            lst[j] = 'O'
    arr.append(lst)
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
l_delta = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
light = [[0] * N for _ in range(N)]
ci = cj = d = 0
for a in A:
    if a == 'F':
        di, dj = delta[d]
        ni, nj = ci+di, cj+dj
        if 0 <= ni < N and 0 <= nj < N:
            if (ni, nj) in zombie and not light[ni][nj] and arr[ni][nj] != 'S':
                print('Aaaaaah!')
                exit(0)
            if arr[ni][nj] == 'S':
                switch(ni, nj)
            ci, cj = ni, nj
    elif a == 'R':
        d = (d-1)%4
    elif a == 'L':
        d = (d+1)%4
    nxt = []
    for z in range(1, num):
        zi, zj = loc[z]
        zd = dr[z]
        di, dj = delta[zd]
        ni, nj = zi+di, zj+dj
        if 0 <= ni < N and 0 <= nj < N:
            loc[z] = (ni, nj)
            nxt.append((ni, nj))
            if (ni, nj) == (ci, cj) and not light[ni][nj]:
                print('Aaaaaah!')
                exit(0)
        else:
            dr[z] = (zd+2)%4
            nxt.append((zi, zj))
    zombie = nxt
print('Phew...')