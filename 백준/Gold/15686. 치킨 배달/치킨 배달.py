from itertools import combinations

'''
풀이 시간 : 3시 ~ 3시 33분
구상 시간 : 15분

아이디어
[1] combination으로 닫은 집 구하고
[2] bfs

첫 번째 시도 : 모든 테스트 케이스 구현 성공 / 시간 초과
오답 이유
[1] bfs를 나눠서 돌려서?
[2] bfs말고 단순 택시거리 총합 시도

수정
[1] 단순 반복문으로 택시거리 계산

두 번째 시도 : 모든 테스트 케이스 구현 성공
'''



def close(s, cl):
    global ans
    dist = 0
    for si, sj in s:
        # 각 집마다 최소 치킨 거리를 구해서
        d = 50*50
        for ci, cj in c:
            if (ci, cj) in cl:
                continue
            d = min(d, abs(ci-si)+abs(cj-sj))
        # 더함
        dist += d

    ans = min(ans, dist)


N, M = map(int, input().split())
arr = []
# 전체 치킨집 수
cnt = 0
# 전체 치킨집 좌표
c = []
# 전체 집 좌표
start = []
for i in range(N):
    lst = list(map(int, input().split()))
    cnt += lst.count(2)
    arr.append(lst)
    for j in range(N):
        if lst[j] == 2:
            c.append((i, j))
        elif lst[j] == 1:
            start.append((i, j))

ans = 50*50*1000

if cnt > M:
    for cl in combinations(c, cnt-M):
        # c 가게들이 폐업했을 때의 치킨 거리
        close(start, cl)
else:
    close(start, [])

print(ans)