H, W = map(int, input().split())
lst = [input() for i in range(H)]


for tc in range(H):
    ans = [-1] * W
    time = 0
    for i in range(W):
        for j in range(i, W):
            if lst[tc][j] == 'c':
                if ans[j] == -1:
                    ans[j] = time
                else:
                    ans[j] = min(ans[j], time)
        lst[tc] = '.' + lst[tc]
        time += 1

    print(*ans)