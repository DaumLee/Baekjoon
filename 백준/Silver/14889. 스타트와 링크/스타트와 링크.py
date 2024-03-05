def score(start):
    global ans

    # 링크 팀
    link = []
    for p in player:
        if p not in start:
            link.append(p)

    sm1 = sm2 = 0
    for i in start:
        for j in start:
            if i == j:
                continue
            sm1 += arr[i][j]

    for i in link:
        for j in link:
            if i == j:
                continue
            sm2 += arr[i][j]

    ans = min(ans, abs(sm1-sm2))


# 모든 조합 찾기 n = 찾은 개수, idx = 마지막 요소의 인덱스, lst = 스타트 팀원
def com(n, idx, lst):
    if len(lst) == N//2:
        # lst = 스타트 팀
        score(lst)
        return

    for i in range(idx+1, N):
        com(n+1, i, lst+[player[i]])


N = int(input())
arr = [[0]*(N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]

player = [i for i in range(1, N+1)]
ans = 10e7

# 모든 조합 찾기
com(0, -1, [])

print(ans)