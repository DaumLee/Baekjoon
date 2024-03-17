def find(v):
    if plst[v] != v:
        plst[v] = find(plst[v])
    return plst[v]


def union(a, b):
    plst[find(b)] = find(a)

N = int(input())
plst = [i for i in range(N+1)]
lst = []
for _ in range(N):
    v1, v2 = map(float, input().split())
    lst.append((v1, v2))

# 모든 정점을 연결하는 간선을 일단 만들고
e = []
for i in range(N-1):
    for j in range(i+1, N):
        e.append((((lst[i][0]-lst[j][0])**2 + (lst[i][1]-lst[j][1])**2)**(1/2), i, j))
# 거리 순 정렬
e.sort()

ans = 0
for item in e:
    c, v1, v2 = item
    if find(v1) != find(v2):
        union(v1, v2)
        ans += c
print(f'{ans:.2f}')