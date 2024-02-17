import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    q = [(0, start)]

    while q:
        cw, cv = heapq.heappop(q)

        # 최단거리가 아니면 진행하지 않음
        if dp[cv] < cw:
            continue

        for dw, nv in lst[cv]:
            nw = cw+dw
            # 최단경로일 경우만 최신화
            if dp[nv] > nw:
                dp[nv] = nw
                heapq.heappush(q, (nw, nv))


N = int(input())
M = int(input())
lst = [list() for _ in range(N+1)]
dp = [N*100000] * (N+1)

# 힙 내 정렬을 위해 가중치를 우선 배치
for i in range(M):
    v1, v2, w = map(int, input().split())
    lst[v1].append((w, v2))

# 출발지와 도착지
s, e = map(int, input().split())
# 출발지에서부터 최단경로 찾기
dijkstra(s)
# 도착지까지의 최단경로 출력
print(dp[e])