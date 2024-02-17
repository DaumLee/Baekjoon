while True:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break
    lst.sort()
    a, b, c = lst[0], lst[1], lst[2]

    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')