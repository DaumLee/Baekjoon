def find(v):
    if p[v] >= 0:
        p[v] = find(p[v])
    else:
        return v
    return p[v]


def union(a, b):
    A, B = find(a), find(b)
    if p[A] >= p[B]:
        p[B] += p[A]
        p[A] = B
        sm[B] += sm[A]
    else:
        p[A] += p[B]
        p[B] = A
        sm[A] += sm[B]


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
time = 0
while True:
    p = [-1] * N**2
    sm = {num: arr[num//N][num%N] for num in range(N**2)}
    for i in range(N):
        for j in range(N):
            if i+1 < N:
                if L <= abs(arr[i][j]-arr[i+1][j]) <= R:
                    if find(i*N+j) != find((i+1)*N+j):
                        union(i*N+j, (i+1)*N+j)
            if j+1 < N:
                if L <= abs(arr[i][j]-arr[i][j+1]) <= R:
                    if find(i*N+j) != find(i*N+j+1):
                        union(i*N+j, i*N+j+1)
    if sum(p) == -N**2:
        break
    for num in range(N**2):
        cnt = -p[find(num)]
        val = sm[find(num)]
        arr[num//N][num%N] = val//cnt
    time += 1
print(time)