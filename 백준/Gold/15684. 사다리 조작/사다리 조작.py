from itertools import combinations


def check(alst):
    # 추가한 사다리로 값 변경하고
    for a in range(len(alst)):
        i, cj, nj = alst[a]
        # 이미 사다리를 둔 칸에는 다시 사다리를 둘 수 없어서 종료
        if route[i][cj] != cj or route[i][nj] != nj:
            # 다시 복구해놓기
            for rep in range(len(alst)):
                i, cj, nj = alst[rep]
                route[i][cj] = cj
                route[i][nj] = nj
            return False
        route[i][cj] = nj
        route[i][nj] = cj
    start = [i for i in range(1, N+1)]
    # 1번부터 N번까지 사다리 시행
    for i in range(1, N+1):
        c = i
        # j번을 거쳐서
        for j in range(H):
            c = route[j][c]
        # 다른 결과가 나왔으면 false
        if start[i-1] != c:
            # 다시 복구해놓기
            for rep in range(len(alst)):
                i, cj, nj = alst[rep]
                route[i][cj] = cj
                route[i][nj] = nj
            return False
    return True


# s = time.time()
N, M, H = map(int, input().split())
route = [{i: i for i in range(1, N+1)} for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    # route[a] = a행에서의 이동 테이블 / route[b] = 목적지 번호
    route[a-1][b] = b+1
    route[a-1][b+1] = b


add = []
for i in range(H):
    for j in range(1, N):
        # 사다리를 둘 수 있으면
        if route[i][j] == j and route[i][j+1] == j+1:
            add.append((i, j, j+1))

L = len(add)
if check([]):
    print(0)
else:
    ans = -1
    flag = 0
    # 추가할 수 있는 사다리 개수가 3개가 안되면 그만큼만 돌리기
    for k in range(1, min(4, L+1)):
        if flag:
            break
        for case in combinations(add, k):
            if check(case):
                ans = len(case)
                flag = 1
                break
    print(ans)

# e = time.time()
# print(e-s)
