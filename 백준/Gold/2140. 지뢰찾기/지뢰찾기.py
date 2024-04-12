N = int(input())
arr = []
for i in range(N):
    lst = list(input())
    for j in range(N):
        if lst[j] != '#':
            lst[j] = int(lst[j])
    arr.append(lst)

c_idx = ((1, 1), (1, N-2), (N-2, 1), (N-2, N-2))
c_check = ((0, 0), (0, N-1), (N-1, 0), (N-1, N-1))
delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

ans = 0
for c in range(4):
    ci, cj = c_idx[c]
    ni, nj = c_check[c]
    if arr[ni][nj] > 0:
        ans += 1
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if type(arr[ni][nj]) is int:
                arr[ni][nj] -= 1

star = 0
for i in range(1, N-1):
    star += int(arr[i][0])
    star += int(arr[0][i])
    star += int(arr[i][N-1])
    star += int(arr[N-1][i])

if N >= 5:
    print(ans+star//3+(N-4)**2)
else:
    print(ans+star//3)