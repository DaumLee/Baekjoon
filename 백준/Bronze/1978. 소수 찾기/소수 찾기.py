def prime(item):
    for i in range(2, item):
        if item % i == 0:
            return 0
    return 1


N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for item in lst:
    if item == 1:
        continue
    cnt += prime(item)
print(cnt)