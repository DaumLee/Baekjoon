from collections import deque

def solve(cd, ri, rj, bi, bj):
    # 위로 기울일 경우
    if cd == 0:
        if ri < bi:
            q = deque([(ri, rj, 0), (bi, bj, 1)])
        else:
            q = deque([(bi, bj, 1), (ri, rj, 0)])
    # 아래로 기울일 경우
    elif cd == 1:
        if ri > bi:
            q = deque([(ri, rj, 0), (bi, bj, 1)])
        else:
            q = deque([(bi, bj, 1), (ri, rj, 0)])
    # 왼쪽으로 기울일 경우
    elif cd == 2:
        if rj < bj:
            q = deque([(ri, rj, 0), (bi, bj, 1)])
        else:
            q = deque([(bi, bj, 1), (ri, rj, 0)])
    # 오른쪽으로 기울일 경우
    else:
        if rj > bj:
            q = deque([(ri, rj, 0), (bi, bj, 1)])
        else:
            q = deque([(bi, bj, 1), (ri, rj, 0)])

    ans = 0
    while q:
        ci, cj, c = q.popleft()
        di, dj = delta[cd]
        while True:
            ni, nj = ci+di, cj+dj
            # 벽이 아니거나 공이 부딪히지 않으면 진행 가능
            if arr[ni][nj] != '#' and not (c == 0 and ni == bi and nj == bj) and not (c == 1 and ni == ri and nj == rj):
                # 공이 구멍에 도착하면 카운트 증가
                if arr[ni][nj] == 'O':
                    # 파란 공이면 해당 조합 불가능
                    if c == 1:
                        return ri, rj, bi, bj, 1
                    # 빨간 공이 도착하면 일단 파란공까지 확인
                    else:
                        # 빨간 공 제거
                        ri = rj = -1
                        ans = 1
                        break
                ci, cj = ni, nj
            else:
                if c == 0:
                    ri, rj = ci, cj
                else:
                    bi, bj = ci, cj
                break
    # 빨간 공만 들어갔으면
    if ans:
        return ri, rj, bi, bj, 2
    # 조건을 만족하지 않았다면 다음도 진행
    else:
        return ri, rj, bi, bj, 0

def product(n, cd, ri, rj, bi, bj):
    global ans
    # 10회를 넘어갈 수 없음
    if n > 10:
        return
    # 최소 시행이 아님
    if n >= ans:
        return
    ri, rj, bi, bj, flag = solve(cd, ri, rj, bi, bj)
    # flag = 0 : 구멍에 아무 공도 들어가지 못함 / flag = 1 : 파란 공이 구멍에 빠짐 / flag = 2 : 빨간 공만 구멍에 들어감
    if flag:
        if flag == 2:
            ans = min(ans, n)
        return
    # 직전과 같은 방향이면 어차피 진행 불가능
    if cd != 0 and not (arr[ri+delta[0][0]][rj+delta[0][1]] == '#' and arr[bi+delta[0][0]][bj+delta[0][1]] == '#'):
        product(n+1, 0, ri, rj, bi, bj)
    if cd != 1 and not (arr[ri+delta[1][0]][rj+delta[1][1]] == '#' and arr[bi+delta[1][0]][bj+delta[1][1]] == '#'):
        product(n+1, 1, ri, rj, bi, bj)
    if cd != 2 and not (arr[ri+delta[2][0]][rj+delta[2][1]] == '#' and arr[bi+delta[2][0]][bj+delta[2][1]] == '#'):
        product(n+1, 2, ri, rj, bi, bj)
    if cd != 3 and not (arr[ri+delta[3][0]][rj+delta[3][1]] == '#' and arr[bi+delta[3][0]][bj+delta[3][1]] == '#'):
        product(n+1, 3, ri, rj, bi, bj)

N, M = map(int, input().split())
arr = []
for i in range(N):
    lst = input()
    for j in range(M):
        if lst[j] == 'B':
            bi, bj = i, j
        elif lst[j] == 'R':
            ri, rj = i, j
    arr.append(lst)

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = 11
for sd in range(4):
    di, dj = delta[sd]
    # 둘다 바로 벽에 막히는 경우는 빼고 조합 진행
    if arr[ri+di][rj+dj] == '#' and arr[bi+di][bj+dj] == '#':
        continue
    product(1, sd, ri, rj, bi, bj)

if ans == 11:
    print(-1)
else:
    print(ans)