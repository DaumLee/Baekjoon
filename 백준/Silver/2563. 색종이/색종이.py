N = int(input())

arr = [[0] * 100 for _ in range(100)]
cnt = 0
for tc in range(1, N+1):
    si, sj = map(int, input().split())
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] = tc

for i in range(100):
    for j in range(100):
        if arr[i][j]:
            cnt += 1

print(cnt)