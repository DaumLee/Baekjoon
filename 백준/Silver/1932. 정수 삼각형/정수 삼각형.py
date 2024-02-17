N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 계속해서 누적합만 저장함, 부모가 있는 두번째 줄부터 시작
for i in range(1, N):
    for j in range(len(graph[i])):
        # 맨 왼쪽은 바로 위 값 더함
        if j == 0:
            graph[i][j] += graph[i-1][j]
        # 맨 오른쪽도 바로 위 값 더함(개수가 하나 적어서 -1 해줌)
        elif j == len(graph[i-1]):
            graph[i][j] += graph[i-1][j-1]
        # 두 부모 중에서 큰 값을 더해서 저장함
        else:
            graph[i][j] += max(graph[i-1][j], graph[i-1][j-1])

# 마지막 노드에서 최댓값 출력
print(max(graph[N-1]))