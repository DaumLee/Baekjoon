def solve(lst, t):
    # print(lst)
    global time

    if t > 1440:
        time = -1
        return

    if sum(lst) == 0:
        time = t
        return

    if len(lst) >= 2:
        # 가장 많이 쌓인 두 집 청소하고
        if lst[1] > 1:
            lst[1] -= 1
        else:
            lst.pop(1)
        if lst[0] > 1:
            lst[0] -= 1
        else:
            lst.pop(0)
        lst.sort(reverse=True)
        solve(lst, t+1)
    else:
        if t+lst[0] <= 1440:
            time = t+lst[0]
        else:
            time = -1
        return


N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
time = 0
solve(lst, 0)
print(time)