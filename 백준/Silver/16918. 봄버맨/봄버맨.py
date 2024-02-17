from collections import deque


def bfs(s):
    q = deque(s)

    while q:
        ci, cj = q.popleft()
        graph[ci][cj] = '.'
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                graph[ni][nj] = '.'


N, M, T = map(int, input().split())
start = []
graph = []
# 폭탄을 저장하고 시작
for i in range(N):
    lst = list(input())
    graph.append(lst)
    for j in range(M):
        if lst[j] == 'O':
            start.append((i, j))

# 최초 1초에서는 아무 것도 하지 않음
for time in range(2, T+1):
    # 2의 배수에서는 폭탄을 채움
    if not time % 2:
        for i in range(N):
            graph[i] = ['O'] * M
    # 홀수번째에서는 폭탄 터트림
    else:
        bfs(start)
        start = []
        # 폭탄을 터트리고 남은 폭탄은 다음 차례에 터트림
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 'O':
                    start.append((i, j))

# 정답 출력
for lst in graph:
    print(''.join(lst))