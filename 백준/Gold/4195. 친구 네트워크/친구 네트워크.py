import sys
input = sys.stdin.readline

def find(v):
    if p[v] >= 0:
        p[v] = find(p[v])
    # 부모 번호가 아니라 집합의 크기를 저장했으니 v를 리턴
    else:
        return v
    return p[v]

def union(a, b):
    a, b = name[a], name[b]
    a, b = find(a), find(b)
    # 같을 수도 있으니 미리 저장해놓고
    ret = abs(p[a])
    # 부모가 다르면
    if a != b:
        # 집합이 큰 쪽에 붙임
        if p[a] <= p[b]:
            p[a] += p[b]
            p[b] = a
            ret = abs(p[a])
        else:
            p[b] += p[a]
            p[a] = b
            ret = abs(p[b])
    print(ret)

for tc in range(int(input())):
    F = int(input())
    # 부모 배열에 집합 크기를 저장
    p = [-1 for i in range(2*F)]
    # 이름을 숫자로 변환
    name = dict()
    # 이름마다 붙여줄 숫자
    num = 0
    for _ in range(F):
        a, b = input().split()
        # 처음 들어온 이름이면 인덱싱
        if a not in name:
            name[a] = num
            num += 1
        # 처음 들어온 이름이면 인덱싱
        if b not in name:
            name[b] = num
            num += 1
        union(a, b)