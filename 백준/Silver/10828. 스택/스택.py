import sys

n = int(sys.stdin.readline())

l = list()

for i in range(n):
    x = sys.stdin.readline().split()
    if x[0] == 'push':
        l.append(x[1])
    elif x[0] == 'pop':
        if l:
            print(l.pop())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(l))
    elif x[0] == 'empty':
        if l:
            print(0)
        else:
            print(1)
    else:
        if l:
            print(l[len(l)-1])
        else:
            print(-1)
