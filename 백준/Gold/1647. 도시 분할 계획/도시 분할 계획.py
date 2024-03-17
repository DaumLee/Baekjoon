import sys
input = sys.stdin.readline

def find(v):
    if plst[v] != v:
        plst[v] = find(plst[v])
    return plst[v]

def union(a, b):
    plst[find(b)] = find(a)

N, M = map(int, input().split())
lst = []
plst = [i for i in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    lst.append((c, a, b))
# 작은 값부터 순회
lst.sort()

ans = 0
for c, v1, v2 in lst:
    # 서로 부모가 다르면
    if find(v1) != find(v2):
        # 두 집합을 합치고
        union(v1, v2)
        ans += c
        # 마을은 두개로 나누어야 하니 다 연결한 후에 제일 큰 비용 간선 하나를 지우면 둘이 됨
        m = c    
print(ans-m)