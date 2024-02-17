N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()

for i in range(N):
    print(*lst[i])