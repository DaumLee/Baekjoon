import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    q = [(0, start)]
    dp[start] = 0

    while q:
        cw, c = heapq.heappop(q)

        if dp[c] < cw:
            continue

        for w, n in graph[c]:
            nw = cw + w
            if nw < dp[n]:
                dp[n] = nw
                heapq.heappush(q, (nw, n))


V, E = map(int, input().split())
K = int(input())

INF = sys.maxsize
dp = [INF]*(V+1)

graph = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((w, v2))

dijkstra(K)

for i in dp[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)