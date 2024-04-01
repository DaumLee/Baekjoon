def check(num):
    ret = [num]
    n = num+1
    while n <= 4:
        if dct[n-1][(base[n-1]+2)%8] != dct[n][(base[n]-2)%8]:
            ret.append(n)
        else:
            break
        n += 1
    n = num-1
    while n > 0:
        if dct[n+1][(base[n+1]-2)%8] != dct[n][(base[n]+2)%8]:
            ret.append(n)
        else:
            break
        n -= 1
    return ret


dct = dict()
for i in range(1, 5):
    dct[i] = list(input())
base = {i: 0 for i in range(1, 5)}
ans = 0
K = int(input())
for _ in range(K):
    num, d = map(int, input().split())
    r = check(num)
    for nxt in r:
        nd = (num-nxt)%2
        if nd:
            base[nxt] = (base[nxt]+d)%8
        else:
            base[nxt] = (base[nxt]-d)%8
for num in range(1, 5):
    if dct[num][base[num]] == '1':
        ans += 2**(num-1)
print(ans)