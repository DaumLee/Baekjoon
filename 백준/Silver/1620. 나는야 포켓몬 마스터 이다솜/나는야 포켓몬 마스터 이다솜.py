N, M = map(int, input().split())
dct1 = dict()
dct2 = dict()

for i in range(N):
    p = input()
    dct1[i+1] = p
    dct2[p] = i+1

for _ in range(M):
    ans = input()
    if ans.isdigit():
        pass
        print(dct1[int(ans)])
    else:
        print(dct2[ans])