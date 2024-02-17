def find(v):
    if p[v] != v:
        p[v] = find(p[v])
    return p[v]


def union(a, b):
    p[find(b)] = find(a)


def kruskal(idx):
    global sm

    # 전체 간선 배열 탐색
    while idx < E:
        e = edge[idx]
        # 간선으로 연결된 노드들이 다른 집합이면
        if find(e[1]) != find(e[2]):
            # 합치고
            union(e[1], e[2])
            sm += e[0]
        # 다음 간선 탐색
        idx += 1


while True:
    V, E = map(int, input().split())
    if V == E == 0:
        break
    # 전체 간선 저장
    edge = []

    # 부모 배열, 최초엔 전부 자기 자신이 부모 노드
    p = [i for i in range(V)]
    for i in range(E):
        v1, v2, w = map(int, input().split())
        edge.append((w, v1, v2))

    # 가중치 오름차순으로 간선 정렬
    edge.sort()

    # 가로등 전체가 켜져있을 때 비용
    mx = 0
    for i in range(E):
        mx += edge[i][0]

    # 최소한으로 남길 가로등의 운용비
    sm = 0
    kruskal(0)

    # 원래 사용량 - 최소 운용비 = 최대 절약
    print(mx-sm)