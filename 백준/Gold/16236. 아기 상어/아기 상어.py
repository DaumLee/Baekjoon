from collections import deque


def adv(si, sj, size, exp):
    # 최초 먹을 수 있는 물고기
    can = []
    # fs = 물고기의 크기
    for fs in fish.keys():
        # 먹을 수 있으면
        if fs < size:
            can.extend(fish[fs])
    time = 0
    ci, cj = si, sj
    while True:
        q = deque([(ci, cj)])
        v = [[0] * N for _ in range(N)]
        v[ci][cj] = 1
        flag = N ** 2 + 1
        ei = ej = -1
        while q:
            ci, cj = q.popleft()
            if v[ci][cj] > flag:
                break
            for di, dj in delta:
                ni, nj = ci+di, cj+dj
                # 이동
                if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and (arr[ni][nj] <= size or arr[ni][nj] == 9):
                    # 먹을 수 있는 물고기를 최초 발견하면 그때까지만 반복
                    if (ni, nj) in can and arr[ni][nj]:
                        if ei != -1:
                            # 더 위의 값이면
                            if ei > ni:
                                ei, ej = ni, nj
                            # 같은 행에서 더 왼쪽 값이면
                            elif ei == ni and ej > nj:
                                ei, ej = ni, nj
                        else:
                            ei, ej = ni, nj
                        flag = v[ci][cj]
                        continue
                    v[ni][nj] = v[ci][cj]+1
                    q.append((ni, nj))
        if ei != -1:
            # 맨 위, 맨 왼쪽을 먹음
            can.remove((ei, ej))
            # 물고기 먹었음
            arr[ei][ej] = 0
            # 경험치 먹음
            exp += 1
            if exp == size:
                exp = 0
                size += 1
                if size-1 in fish:
                    can.extend(fish[size-1])
            # print((ei, ej), flag)
            time += flag
            ci, cj = ei, ej
        else:
            break
    print(time)


N = int(input())
arr = []
size = 2
fish = dict()
# 전체 물고기 수
# fish_cnt = 0
for i in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)
    for j in range(N):
        if lst[j] == 9:
            si, sj = i, j
        elif lst[j]:
            # 이미 같은 사이즈의 물고기가 있다면
            if lst[j] in fish:
                fish[lst[j]].append((i, j))
            # 없으면 생성
            else:
                fish[lst[j]] = [(i, j)]
            # fish_cnt += 1

delta = ((0, -1), (-1, 0), (1, 0), (0, 1))

adv(si, sj, size, 0)