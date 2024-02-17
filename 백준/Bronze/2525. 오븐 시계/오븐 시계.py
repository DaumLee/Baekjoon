import sys

a, b, c = map(int, sys.stdin.read().split())

m = b+c
h = a + m//60


if b+c < 60:
    print(a, b+c)
else:
    if h > 23:
        print(h % 24, m % 60)
    else:
        print(h, m % 60)