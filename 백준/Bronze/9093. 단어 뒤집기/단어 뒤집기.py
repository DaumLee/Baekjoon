N = int(input())

for _ in range(N):
    lst = list(input().split())

    for i in lst:
        print(i[::-1], end=' ')
    print()