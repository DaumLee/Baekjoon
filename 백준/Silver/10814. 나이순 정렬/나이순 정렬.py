N = int(input())
lst = []

for i in range(N):
    ipt = list(input().split())
    lst.append([int(ipt[0]), i, ipt[1]])

lst.sort()

for i in range(N):
    print(lst[i][0], lst[i][2])