def dfs(ci, cj, cnt):
    global mx

    mx = max(mx, cnt)
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci+di, cj+dj
        if 0 <= ni < N and 0 <= nj < M and not v[ord(arr[ni][nj])-65]:
            v[ord(arr[ni][nj])-65] = 1
            dfs(ni, nj, cnt+1)
            # 원복
            v[ord(arr[ni][nj])-65] = 0

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# 알파벳 방문 여부 확인
v = [0]*26
v[ord(arr[0][0])-65] = 1
mx = 1
dfs(0, 0, 1)
print(mx)