import sys

l = [i for i in range(1, 31)]

for _ in range(28):
    i = int(sys.stdin.readline())
    l.remove(i)

for i in range(len(l)):
    print(l[i], end=" ")