import sys

x = int(sys.stdin.readline())

l = [64]


def stick(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum


while True:
    ans = stick(l)

    if ans > x:
        idx = l.index(min(l))
        l[idx] /= 2
        if stick(l) >= x:
            pass
        else:
            l.append(l[idx])

    elif ans == x:
        print(len(l))
        exit()