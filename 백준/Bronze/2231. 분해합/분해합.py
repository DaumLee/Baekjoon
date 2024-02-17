N = int(input())

for i in range(N):
    item = sm = i
    for j in range(len(str(i))):
        sm += (item % 10)
        item //= 10
    if sm == N:
        print(i)
        break
else:
    print(0)