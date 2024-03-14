def turn(x, d, k):
    for i in range(N):
        lst = arr[i]
        # 배수가 아니면 회전하지 않음
        if (i+1) % x:
            continue
        # 반시계 회전
        if d == 0:
            for _ in range(k):
                lst = [lst[M-1]]+lst[:M-1]
        # 시계 회전
        else:
            for _ in range(k):
                lst = lst[1:]+[lst[0]]
        arr[i] = lst

    # 인접 수가 있는지 확인
    chk = 0
    v = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                for di, dj in delta:
                    ni, nj = i+di, (j+dj)%M
                    if 0 <= ni < N and arr[ni][nj]:
                        if arr[i][j] == arr[ni][nj]:
                            v[i][j] = v[ni][nj] = 1
                            chk = 1
        # if arr[i][0] == arr[i][M-1]:
        #     v[i][0] = v[i][M-1] = 1

    if not chk:
        sm = 0
        cnt = 0
        for i in range(N):
            sm += sum(arr[i])
            for j in range(M):
                if arr[i][j] != 0:
                    cnt += 1
        if cnt > 0:
            avg = sm / cnt
            for i in range(N):
                for j in range(M):
                    if arr[i][j]:
                        if arr[i][j] > avg:
                            arr[i][j] -= 1
                        elif arr[i][j] < avg:
                            arr[i][j] += 1
        return

    for i in range(N):
        for j in range(M):
            if v[i][j]:
                arr[i][j] = 0


N, M, T = map(int, input().split())
arr = []
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
for i in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)

for _ in range(T):
    x, d, k = map(int, input().split())
    turn(x, d, k)

sm = 0
for i in range(N):
    sm += sum(arr[i])
print(sm)