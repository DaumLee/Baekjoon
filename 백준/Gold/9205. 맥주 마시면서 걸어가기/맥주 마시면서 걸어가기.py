from collections import deque

def bfs(s):
    sj, si = s
    q = deque()
    q.append((sj, si))
    # 방문한 지점을 저장
    v = set()
    v.add((sj, si))

    while q:
        cj, ci = q.popleft()
        # 도착 가능하면 리턴
        if abs(ci-end[1]) + abs(cj-end[0]) <= 1000:
            return "happy"
        # 편의점 루프
        for i in range(n):
            # 편의점 방문 안했으면
            if spot[i] not in v:
                nj, ni = spot[i]
                # 거리도 갈 수 있으면
                if abs(ni-ci) + abs(nj-cj) <= 1000:
                    v.add((nj, ni))
                    q.append((nj, ni))
    return "sad"


t = int(input())

for tc in range(t):
    n = int(input())
    # 출발
    start = list(map(int, input().split()))
    spot = []
    for _ in range(n):
        j, i = map(int, input().split())
        # 편의점 저장
        spot.append((j, i))
    # 도착
    end = list(map(int, input().split()))

    print(bfs(start))