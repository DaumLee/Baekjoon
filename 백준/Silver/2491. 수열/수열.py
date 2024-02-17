import sys

n = int(input())
lst = list(map(int, input().split()))

mx = 0
l = 1
for i in range(n-1):
    if lst[i] <= lst[i+1]:
        l += 1
    else:
        mx = max(l, mx)
        l = 1
else:
    mx = max(l, mx)

l = 1
lst = lst[::-1]

for i in range(n-1):
    if lst[i] <= lst[i+1]:
        l += 1
    else:
        mx = max(l, mx)
        l = 1
else:
    mx = max(l, mx)

print(mx)