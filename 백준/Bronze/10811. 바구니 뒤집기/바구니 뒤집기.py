import sys

n, m = map(int, sys.stdin.readline().split())
l = [a for a in range(1, n+1)]

for _ in range(1, m+1):
    i, j = map(int, sys.stdin.readline().split())
    rev = l[i-1:j]
    rev.reverse()
    l[i-1:j] = rev

for index in range(n):
    print(l[index], end=" ")