import sys

a, b = map(int, sys.stdin.read().split())

if a > 0:
    if b > 0:
        print(1)
    else:
        print(4)
else:
    if b > 0:
        print(2)
    else:
        print(3)