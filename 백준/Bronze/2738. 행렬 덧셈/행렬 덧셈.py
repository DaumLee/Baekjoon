import sys

n, m = map(int, sys.stdin.readline().split())

l1 = [0 for _ in range(n)]
l2 = [0 for _ in range(n)]
mat = [[0 for _ in range(m)] for j in range(n)]

for i in range(n):
    l1[i] = sys.stdin.readline().split()

for i in range(n):
    l2[i] = sys.stdin.readline().split()

for i in range(n):
    for j in range(m):
        mat[i][j] = int(l1[i][j]) + int(l2[i][j])

for i in range(n):
    for j in range(m):
        print(mat[i][j], end=" ")
    print()