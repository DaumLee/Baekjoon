from collections import deque

N, L = map(int, input().split())
lst = list(map(int, input().split()))
cand = deque()
idx = deque()
ans = []
for i in range(N):
    while cand and cand[-1] > lst[i]:
        cand.pop()
        idx.pop()
    cand.append(lst[i])
    idx.append(i)
    if idx[0] < i-L+1:
        idx.popleft()
        cand.popleft()
    ans.append(cand[0])
print(*ans)