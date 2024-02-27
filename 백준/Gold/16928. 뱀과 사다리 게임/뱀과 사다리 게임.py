from collections import deque


def bfs(s):
    global ans

    q = deque([s])
    v = [0] * 100
    v[s] = 1

    while q:
        c = q.popleft()
        if c == 99:
            ans = min(ans, v[c]-1)
        for d in (1, 2, 3, 4, 5, 6):
            n = c+d
            # 갈 수 있고 최단 거리면 ㄱㄱ
            if n < 100 and (not v[n] or v[c]+1 < v[n]):
                v[n] = v[c] + 1
                # 사다리 타면 도착지도 같은 횟수 만큼 주사위 굴린 것
                if n in ls:
                    nn = le[ls.index(n)]
                    # 최단거리일 떄만
                    if not v[nn] or v[nn] > v[n]:
                        v[nn] = v[n]
                        q.append(nn)
                # 뱀 타면 추진력 얻으러 뒤로 감
                elif n in ss:
                    nn = se[ss.index(n)]
                    # 최단거리일 때만
                    if not v[nn] or v[nn] > v[n]:
                        v[nn] = v[n]
                        q.append(nn)
                # 아무 것도 없으면 그대로 진행
                else:
                    q.append(n)


N, M = map(int, input().split())
board = [i for i in range(100)]
# 주사위 횟수의 최댓값
ans = 100
# 사다리의 시작점과 도착점
ls = []
le = []
for _ in range(N):
    s, e = map(int, input().split())
    ls.append(s-1)
    le.append(e-1)

# 뱀의 시작점
ss = []
se = []
for _ in range(M):
    s, e = map(int, input().split())
    ss.append(s-1)
    se.append(e-1)

bfs(0)
print(ans)