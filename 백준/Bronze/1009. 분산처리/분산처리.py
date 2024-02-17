import sys

t = int(sys.stdin.readline())

list = [[10], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    i = a % 10
    index = b % len(list[i])
    print(list[i][index])