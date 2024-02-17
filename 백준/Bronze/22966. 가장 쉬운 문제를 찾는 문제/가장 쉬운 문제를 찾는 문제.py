N = int(input())

lst = [input().split()[::-1] for _ in range(N)]
lst.sort()

print(lst[0][1])