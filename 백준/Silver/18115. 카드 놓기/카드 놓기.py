from collections import deque

N = int(input())
odr = list(map(int, input().split()))
ans = [0 for i in range(N)]
v = deque()
for i in range(N):
    v.append(i)

for i in range(N):
    if odr[i] == 1:
        ans[v.popleft()] = N-i
    elif odr[i] == 2:
        ans[v[1]] = N-i
        del v[1]
    else:
        ans[v.pop()] = N-i

print(*ans)