import sys

n, m = map(int, sys.stdin.readline().split())
ans = [0 for _ in range(n)]

for a in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for b in range(i, j+1):
        ans[b-1] = k

for i in range(n):
    print(ans[i], end=" ")