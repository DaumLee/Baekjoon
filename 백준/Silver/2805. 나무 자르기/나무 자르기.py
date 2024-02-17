def bs(n):
    global ans
    s, e = 0, max(lst)-1

    while s <= e:
        m = (s+e)//2
        sm = 0
        for i in range(N):
            # 자를 수 있으면 잘라서 가져감
            if lst[i] > m:
                sm += lst[i]-m
            # 자를 수 없게 되면 종료
            else:
                break

        # 자른 나무가 목적을 달성하면 정답과 비교하고 출발지를 앞으로 보냄(sm을 줄임)
        if sm >= M:
            ans = max(ans, m)
            s = m+1
        # 자른 나무 합계가 M보다 작으면 최대 높이를 줄임(sm을 늘림)
        elif sm < M:
            e = m-1


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
ans = 0
bs(M)
print(ans)