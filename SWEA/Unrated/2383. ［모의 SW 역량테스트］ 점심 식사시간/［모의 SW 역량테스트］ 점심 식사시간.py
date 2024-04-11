import heapq


def down(lst):
    query = []
    for i in range(len(lst)):
        ci, cj = loc[i]
        ei, ej, K = end[lst[i]]
        heapq.heappush(query, (abs(ci - ei) + abs(cj - ej), lst[i], K, 0))

    # 계단 내려가는 사람 수
    v = [0, 0]
    # 계단을 다 내려갈 때까지 남은 시간
    time = [[], []]
    # 나간 사람 수
    cnt = 0
    now = -1
    while cnt < len(loc):
        if query:
            t, stair, K, arrived = heapq.heappop(query)
            if now == -1: now = t
        else:
            t, stair = now+1, -1
        if now != t:
            for s in range(2):
                if v[s]:
                    r = 0
                    for p in range(len(time[s])):
                        time[s][p] -= t - now
                        if time[s][p] <= 0:
                            v[s] -= 1
                            r += 1
                    for _ in range(r):
                        time[s].pop(0)
                    cnt += r
        if stair != -1:
            if v[stair] < 3:
                if arrived:
                    time[stair].append(K)
                    heapq.heappush(query, (t+K, -1, -1, 1))
                else:
                    time[stair].append(K+1)
                    heapq.heappush(query, (t+K+1, -1, -1, 1))
                v[stair] += 1
            else:
                heapq.heappush(query, (t+1, stair, K, 1))
        now = t
    return now


def divide(lst):
    global ans

    if len(lst) == len(loc):
        ans = min(ans, down(lst))
        return

    for i in range(2):
        divide(lst + [i])


for tc in range(1, int(input()) + 1):
    N = int(input())
    loc = []
    end = []
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            if lst[j] == 1:
                loc.append((i, j))
            elif lst[j] >= 2:
                end.append((i, j, lst[j]))
    ans = 21e8
    divide([])
    print(f'#{tc} {ans}')