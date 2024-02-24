def solve(root):
    from collections import deque
    q = deque([root])

    while q:
        p = q.popleft()
        # 부모의 자식 탐색
        for s in graph[p]:
            # 부모가 공백이면
            if ans[s] == 0:
                # 부모 등록
                ans[s] = p
                q.append(s)


N = int(input())
graph = [list() for _ in range(N+1)]

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

ans = [0] * (N+1)
# 루트부터 자식 찾기 시작
solve(1)
print(*ans[2:], sep='\n')