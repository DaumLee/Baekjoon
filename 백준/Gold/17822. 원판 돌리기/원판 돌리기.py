def check():
    flag = 0
    v = {i: [0] * M for i in range(1, N+1)}
    for i in range(1, N+1):
        for j in range(M):
            if not arr[i][j]: continue
            if arr[i][j] == arr[i][(j+1)%M]:
                v[i][j] = v[i][(j+1)%M] = 1
                flag = 1
            if i < N and arr[i][j] == arr[i+1][j]:
                v[i][j] = v[i+1][j] = 1
                flag = 1
    if flag:
        for i in range(1, N+1):
            for j in range(M):
                if v[i][j]:
                    arr[i][j] = 0
    else:
        sm = cnt = 0
        for i in range(1, N+1):
            sm += sum(arr[i])
            for j in range(M):
                if arr[i][j]:
                    cnt += 1
        if not cnt: return
        avg = sm/cnt
        for i in range(1, N+1):
            for j in range(M):
                if arr[i][j] and arr[i][j] > avg:
                    arr[i][j] -= 1
                elif arr[i][j] and arr[i][j] < avg:
                    arr[i][j] += 1


N, M, Q = map(int, input().split())
arr = dict()
num = 1
for _ in range(N):
    lst = list(map(int, input().split()))
    arr[num] = lst
    num += 1
for _ in range(Q):
    x, d, k = map(int, input().split())
    if d == 0:
        for i in range(1, N+1):
            if not i%x:
                for _ in range(k):
                    arr[i] = [arr[i][-1]] + arr[i][:-1]
    else:
        for i in range(1, N+1):
            if not i % x:
                for _ in range(k):
                    arr[i] = arr[i][1:] + [arr[i][0]]
    check()
ans = 0
for i in range(1, N+1):
    ans += sum(arr[i])
print(ans)