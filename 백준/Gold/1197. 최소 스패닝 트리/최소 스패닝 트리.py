def union(a, b):
    p[find(b)] = find(a)


def find(v):
    if p[v] != v:
        p[v] = find(p[v])
    return p[v]


def kruskal(e):
    global sm

    idx = e
    while idx < E:
        e = edge[idx]
        # 사이클이 형성되지 않으면
        if find(e[1]) != find(e[2]):
            sm += e[0]
            union(e[1], e[2])
        # 다음 간선 체크
        idx += 1


V, E = map(int, input().split())
edge = []
p = [i for i in range(V+1)]
for _ in range(E):
    v1, v2, w = map(int, input().split())
    edge.append((w, v1, v2))

# 가중치의 오름차순 정렬
edge.sort()
# 가중치 최댓값
sm = 0
kruskal(0)

print(sm)