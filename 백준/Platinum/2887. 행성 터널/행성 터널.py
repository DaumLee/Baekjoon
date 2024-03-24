import sys
input = sys.stdin.readline

def find(v):
    if p[v] != v:
        p[v] = find(p[v])
    return p[v]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        p[b] = a

N = int(input())
# 행성 리스트
xs = []
ys = []
zs = []
for i in range(N):
    x, y, z = map(int, input().split())
    xs.append((x, i))
    ys.append((y, i))
    zs.append((z, i))

xs.sort()
ys.sort()
zs.sort()

# 간선 구하고
e = []
for i in range(N-1):
    # 바로 옆 좌표끼리만 연결(먼 좌표는 연결하지 않음)
    # 이게 MST를 보장할 수 있나?
    e.append((abs(xs[i][0] - xs[i+1][0]), xs[i][1], xs[i+1][1]))
    e.append((abs(ys[i][0] - ys[i+1][0]), ys[i][1], ys[i+1][1]))
    e.append((abs(zs[i][0] - zs[i+1][0]), zs[i][1], zs[i+1][1]))
e.sort()

# 초기 부모 배열 세팅
p = [i for i in range(N)]
ans = 0
for cost, a, b in e:
    if find(a) != find(b):
        union(a, b)
        ans += cost
print(ans)