def printmap(arr):
    for i in range(N):
        for j in range(N):
            print(f'{arr[i][j]:>2}', end=' ')
        print()
    print()


def numbering(lst):
    arr = [[0] * N for _ in range(N)]
    length = 1
    ci, cj = si, sj
    arr[ci][cj] = 0
    cd = 3
    go = 0
    idx = 1
    while True:
        if length > N-1:
            break
        for k in range(length):
            di, dj = delta[cd]
            ni, nj = ci+di, cj+dj
            arr[ni][nj] = lst[idx]
            idx += 1
            ci, cj = ni, nj
        cd = turn[cd]
        go += 1
        if go == 2:
            go = 0
            length += 1
    for k in range(N-1):
        di, dj = delta[cd]
        ni, nj = ci+di, cj+dj
        arr[ni][nj] = lst[idx]
        idx += 1
        ci, cj = ni, nj
    return arr


def indexing(arr):
    lst = [0]
    length = 1
    ci, cj = si, sj
    cd = 3
    go = 0
    while True:
        if length > N-1:
            break
        for k in range(length):
            di, dj = delta[cd]
            ni, nj = ci+di, cj+dj
            lst.append(arr[ni][nj])
            ci, cj = ni, nj
        cd = turn[cd]
        go += 1
        if go == 2:
            go = 0
            length += 1
    for k in range(N-1):
        di, dj = delta[cd]
        ni, nj = ci+di, cj+dj
        lst.append(arr[ni][nj])
        ci, cj = ni, nj
    return lst


def find_idx(ei, ej):
    num = 0
    length = 1
    ci, cj = si, sj
    cd = 3
    go = 0
    while True:
        if length > N-1:
            break
        for k in range(length):
            di, dj = delta[cd]
            ni, nj = ci+di, cj+dj
            # 목적지를 찾으면 목적지의 1차원 배열 인덱스를 리턴
            if ni == ei and nj == ej:
                return num+1
            num += 1
            ci, cj = ni, nj
        cd = turn[cd]
        go += 1
        if go == 2:
            go = 0
            length += 1
    for dl in range(1, N):
        di, dj = delta[cd]
        ni, nj = ci+di, cj+dj
        # 목적지를 찾으면 목적지의 1차원 배열 인덱스를 리턴
        if ni == ei and nj == ej:
            return num+dl
        ci, cj = ni, nj


def blizard(d, s):
    remove = []
    # cnt = 0
    di, dj = delta[d]
    for k in range(1, s+1):
        ni, nj = si+di*k, sj+dj*k
        if 0 <= ni < N and 0 <= nj < N:
            # 구슬 파괴
            # 파괴는 점수로 세지 않음
            # ans[arr[ni][nj]] += 1
            arr[ni][nj] = 0
            remove.append(find_idx(ni, nj))
            # 뒤에 0 추가
            lst.append(0)
            # cnt += 1
    while remove:
        item = remove.pop()
        lst.pop(item)
    # return cnt


def fill():
    length = 1
    ci, cj = si, sj
    cd = 3
    go = 0
    while True:
        if length > N-1:
            break
        for k in range(length):
            di, dj = delta[cd]
            ni, nj = ci+di, cj+dj
            # 빈칸을 발견
            if not arr[ci][cj]:
                arr[ci][cj] = arr[ni][nj]
                arr[ni][nj] = 0
            ci, cj = ni, nj
        cd = turn[cd]
        go += 1
        if go == 2:
            go = 0
            length += 1
    for k in range(N-1):
        di, dj = delta[cd]
        ni, nj = ci+di, cj+dj
        ci, cj = ni, nj


def bomb(init=0):
    new_lst = []
    flag = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            continue
        cnt = 1
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                cnt += 1
            else:
                if cnt >= 4:
                    flag = 1
                    for k in range(i, i+cnt):
                        ans[lst[k]] += 1
                        lst[k] = 0
                break
        # 수정 (7시 49분)
        else:
            if cnt >= 4:
                flag = 1
                for k in range(i, i + cnt):
                    ans[lst[k]] += 1
                    lst[k] = 0
    for i in lst:
        if i:
            new_lst.append(i)
    if flag or init:
        return new_lst


def grouping():
    new_lst = [0]
    v = [0] * len(lst)
    for i in range(len(lst)):
        if len(new_lst) >= N**2:
            return new_lst
        if v[i]:
            continue
        cnt = 1
        v[i] = 1
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                cnt += 1
                v[j] = 1
            else:
                new_lst.append(cnt)
                new_lst.append(lst[i])
                break
        else:
            new_lst.append(cnt)
            new_lst.append(lst[i])
    if lst and not v[len(lst)-1]:
        new_lst.append(1)
        new_lst.append(lst[-1])
    return new_lst


N, M = map(int, input().split())
# 상어 시작 위치
si = sj = N//2
delta = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
turn = {1: 3, 2: 4, 3: 2, 4: 1}
arr = [list(map(int, input().split())) for _ in range(N)]
lst = indexing(arr)
# 빈칸, 1번 구슬, 2번 구슬, 3번 구슬 파괴 개수
ans = [0, 0, 0, 0]

for _ in range(M):
    d, s = map(int, input().split())
    # 부순 구슬 총 개수
    blizard(d, s)
    # 최초 문자열 폭발 시행 후
    lst = bomb(1)
    # 계속 문자열 폭발
    while True:
        a = bomb()
        if a: lst = a
        else: break
    new_lst = grouping()
    # 패딩 완료
    nxt_lst = [0] * N**2
    for i in range(min(len(new_lst), len(nxt_lst))):
        nxt_lst[i] = new_lst[i]
    lst = nxt_lst
    arr = numbering(lst)
    # printmap(arr)

sm = 0
for i in range(1, 4):
    sm += i*ans[i]
print(sm)