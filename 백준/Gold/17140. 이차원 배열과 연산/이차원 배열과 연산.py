def sorting():
    nxt = []
    mx = 0
    for lst in arr:
        chk = []
        ret = []
        for i in range(len(lst)):
            if lst[i] and lst[i] not in chk:
                chk.append(lst[i])
                ret.append([lst[i], lst.count(lst[i])])
        ret.sort(key=lambda x: (x[1], x[0]))
        nxt.append([])
        for item in ret:
            nxt[-1].extend(item)
        nxt[-1] = nxt[-1][:100]
        mx = max(mx, len(nxt[-1]))
    for i in range(len(nxt)):
        if len(nxt[i]) < mx:
            nxt[i] += [0]*(mx-len(nxt[i]))
    return nxt


ei, ej, K = map(int, input().split())
ei, ej = ei-1, ej-1
arr = [list(map(int, input().split())) for _ in range(3)]
time = 0
while time < 101:
    # 범위 체크
    if ei < len(arr) and ej < len(arr[0]):
        if arr[ei][ej] == K:
            break
    time += 1
    if len(arr) < len(arr[0]):
        arr = list(map(list, zip(*arr)))[::-1]
        arr = sorting()
        arr = list(map(list, zip(*arr[::-1])))
    else:
        arr = sorting()
    continue
if time == 101:
    print(-1)
else:
    print(time)