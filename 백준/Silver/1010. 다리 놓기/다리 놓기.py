import sys

t = int(sys.stdin.readline())


def f(n):
    if n > 1:
        return n * f(n-1)
    else:
        return 1


for _ in range(t):
    n, m = sys.stdin.readline().split()
    print(f(int(m)) // (f(int(n)) * f(int(m)-int(n))))