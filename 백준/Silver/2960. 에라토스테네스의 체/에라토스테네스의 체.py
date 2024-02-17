n, k = map(int,input().split())

rtn = [0 for i in range(n+1)]

cnt = 0

for i in range(2,n+1):
    if rtn[i] == 1:
        continue
    for j in range(i, n+1, i):
        if rtn[j] == 0:
            rtn[j] = 1
            cnt += 1
            if cnt == k:
                print(j)
                break