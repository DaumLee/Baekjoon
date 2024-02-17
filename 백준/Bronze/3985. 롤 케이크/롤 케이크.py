import sys

l = int(input())
n = int(input())

roll = [0 for _ in range(l)]
wish = [0 for _ in range(n)]
cnt = [0 for _ in range(n)]

for i in range(1, n+1):
    p, k = map(int, input().split())
    for j in range(p-1, k):
        if roll[j] == 0:
            roll[j] = i
    wish[i-1] = k - p
    cnt[i-1] = roll.count(i)

print(wish.index(max(wish))+1)
print(cnt.index(max(cnt))+1)