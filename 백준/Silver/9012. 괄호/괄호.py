t = int(input())
for _ in range(t):
    x = input()

    l, r = 0, 0

    for i in range(len(x)):
        if l-r < 0:
            l = -1
            break
        if x[i] == '(':
            l += 1
        else:
            r += 1

    if l == r:
        print('YES')
    else:
        print('NO')