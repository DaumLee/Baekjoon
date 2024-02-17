N = int(input())
lst = []
for _ in range(N):
    p = input().split()
    if p[1] == 'enter':
        lst.append(p[0])
    else:
        lst.remove(p[0])

lst.sort(reverse=True)

for i in lst:
    print(i)