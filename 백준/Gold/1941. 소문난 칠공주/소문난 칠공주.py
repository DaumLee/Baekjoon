def connected(tlst):
    # 모든 칸을 방문 처리 후
    v = [1] * 25
    # 조합에 속한 인원만 미방문 표기
    for idx in tlst:
        v[idx] = 0

    from collections import deque
    # 리스트의 첫 좌표를 큐에 넣고
    q = deque([tlst[0]])
    # 방문 개수 셈
    cnt = 0

    while q:
        ci = q.popleft()
        # -1, 1이면 옆으로 연결 / -5, 5면 위 아래로 연결
        for di in (-1, 1, -5, 5):
            # 오른쪽 끝과 왼쪽 끝은 아래 행이기 때문에 연결되어 있지 않음
            if ci % 5 == 4 and di == 1:
                continue
            # 왼쪽 끝의 왼쪽은 윗 행이기 때문에 연결되어 있지 않음
            elif ci % 5 == 0 and di == -1:
                continue
            ni = ci+di
            # 방문한 적이 없으면 방문
            if 0 <= ni < 25 and not v[ni]:
                v[ni] = 1
                q.append(ni)
                # 1칸 방문 성공
                cnt += 1

    # 모두 연결되어 있으면
    if cnt == 7:
        return 1
    # 조합이 연결되지 않았으면
    else:
        return 0


# n개 뽑음 / 1차원 인덱스 / 임도연파 카운트 / 조합 인덱스 저장 배열
def solve(n, ci, y, tlst):
    global ans

    # y가 넷 이상이면 리턴
    if y >= 4:
        return

    # 7명 다 뽑았으면
    if n == 7:
        # 조합이 연결 돼있나 확인 후 카운트
        if connected(tlst):
            ans += 1
        return

    for ni in range(ci+1, 25):
        tlst.append(ni)
        # 임도연파면 y +1
        if graph[ni] == 'Y':
            solve(n+1, ni, y+1, tlst)
        else:
            solve(n+1, ni, y, tlst)
        tlst.pop()


graph = []
# 입력값을 1차원으로 연결함
for i in range(5):
    lst = list(input())
    graph.extend(lst)

ans = 0
solve(0, -1, 0, [])
print(ans)