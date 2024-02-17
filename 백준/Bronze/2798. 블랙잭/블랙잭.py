N, M = map(int, input().split())

lst = list(map(int, input().split()))
mx = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sm = lst[i] + lst[j] + lst[k]
            if sm <= M:
                mx = max(sm, mx)

print(mx)