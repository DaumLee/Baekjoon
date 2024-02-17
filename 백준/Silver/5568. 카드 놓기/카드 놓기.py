def solve(n, st, idx):
    global ans
    if n == K:
        ans.add(st)
        return

    for i in range(N):
        if i not in idx:
            solve(n+1, st+str(lst[i]), idx+[i])


N = int(input())
K = int(input())
lst = []
ans = set()
for i in range(N):
    lst.append(int(input()))

solve(0, '', [])
print(len(ans))