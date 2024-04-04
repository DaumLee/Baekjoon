def press():
    nxt = [lst[:] for lst in arr]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i < len(arr)-1:
                if arr[i][j] and arr[i+1][j]:
                    d = abs(arr[i][j]-arr[i+1][j])//5
                    if arr[i][j] > arr[i+1][j]:
                        nxt[i][j] -= d
                        nxt[i+1][j] += d
                    else:
                        nxt[i+1][j] -= d
                        nxt[i][j] += d
            if j < len(arr[i])-1:
                if arr[i][j] and arr[i][j+1]:
                    d = abs(arr[i][j] - arr[i][j+1]) // 5
                    if arr[i][j] > arr[i][j+1]:
                        nxt[i][j] -= d
                        nxt[i][j+1] += d
                    else:
                        nxt[i][j+1] -= d
                        nxt[i][j] += d
    lst = []
    for j in range(len(nxt[0])):
        for i in range(len(nxt) - 1, -1, -1):
            if nxt[i][j]:
                lst.append(nxt[i][j])
    return lst

N, K = map(int, input().split())
lst = list(map(int, input().split()))
time = 0
while True:
    time += 1
    # 밀가루 추가
    mn = min(lst)
    for i in range(len(lst)):
        if lst[i] == mn: lst[i] += 1
    # 말기
    length = 1
    tmp, lst = lst[:length], lst[length:]
    cnt = 1
    tmp += [0]*(len(lst)-len(tmp))
    arr = [tmp]+[lst]
    while True:
        tmp = [lst[:length] for lst in arr]
        tmp = list(map(list, zip(*tmp[::-1])))
        lst = arr[-1][length:]
        if len(tmp[0]) > len(lst):
            break
        cnt += 1
        for i in range(len(tmp)):
            tmp[i] += [0]*(len(lst)-len(tmp[i]))
        arr = tmp+[lst]
        if cnt == 2:
            cnt = 0
            length += 1
    # 도우 누르기
    lst = press()
    # 도우 두 번 반으로 접기
    left = lst[:len(lst)//2]
    right = lst[len(lst)//2:]
    arr = [left[::-1]]+[right]
    left = [lst[:len(arr[0])//2] for lst in arr]
    left = list(map(list, zip(*left[::-1])))
    left = list(map(list, zip(*left[::-1])))
    right = [lst[len(arr[0])//2:] for lst in arr]
    arr = left+right
    lst = press()
    if max(lst)-min(lst) <= K:
        break
print(time)