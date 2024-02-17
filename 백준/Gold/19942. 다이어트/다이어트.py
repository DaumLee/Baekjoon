def solve(n, p, c, f, v, cost, tlst):
    global ans, nums

    if n == N:
        # 기준치를 통과하면 정답 갱신
        if p >= lst[0] and c >= lst[1] and f >= lst[2] and v >= lst[3] and cost <= ans:
            ans = cost
            nums = tlst
        return

    # 모두 기준치를 통과하면 추가로 담지 않음
    solve(n+1, p, c, f, v, cost, tlst)
    # 하나라도 기준치를 통과하지 못하면 추가로 담을 수 있음
    if p < lst[0] or c < lst[1] or f < lst[2] or v < lst[3]:
        solve(n+1, p+graph[n][0], c+graph[n][1], f+graph[n][2], v+graph[n][3], cost+graph[n][4], tlst+[n])


N = int(input())
lst = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 500 * N + 1
nums = []
solve(0, 0, 0, 0, 0, 0, [])

if ans == 500 * N + 1:
    print(-1)
else:
    print(ans)
    for i in nums:
        print(i+1, end=' ')