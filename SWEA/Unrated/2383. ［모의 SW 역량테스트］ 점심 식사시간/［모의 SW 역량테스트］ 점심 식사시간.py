import heapq


def down(lst):
    query = []
    for i in range(len(lst)):
        ci, cj = loc[i]
        ei, ej, K = end[lst[i]]
        # 거리, 계단 번호, 계단을 내려갈 때까지 걸리는 시간, 계단 입구 도착 여부를 힙큐에 저장
        heapq.heappush(query, (abs(ci-ei) + abs(cj-ej), lst[i], K, 0))

    # 계단 내려가는 사람 수
    v = [0, 0]
    # 계단을 다 내려갈 때까지 남은 시간
    time = [[], []]
    # 나간 사람 수
    cnt = 0
    # 현재 시간
    now = -1
    while cnt < len(loc):
        # 쿼리에 값이 있으면 시간 점프
        if query:
            t, stair, K, arrived = heapq.heappop(query)
            # 최초 시간을 현재 시간과 동기화
            if now == -1: now = t
        # 더이상 쿼리가 없으면 시간을 1씩 증가
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
        # 계단을 들어가려고 시도하는 경우
        if stair != -1:
            # 계단에 들어갈 수 있으면
            if v[stair] < 3:
                # 계단 입구에서 대기 중이면 K시간 뒤 완료
                if arrived:
                    time[stair].append(K)
                    heapq.heappush(query, (t+K, -1, -1, 1))
                # 계단 입구에 지금 막 도착했으면 K+1시간 뒤 완료
                else:
                    time[stair].append(K+1)
                    heapq.heappush(query, (t+K+1, -1, -1, 1))
                v[stair] += 1
            # 다음 시간에 다시 시도, 계단 입구에는 도착해 있음
            else:
                heapq.heappush(query, (t+1, stair, K, 1))
        # 시간 동기화
        now = t
    return now


def divide(lst):
    global ans

    # 사람이 어떤 계단으로 들어갈 지 모두 정했으면
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