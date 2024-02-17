import sys
input = sys.stdin.readline


def binary_search(lst, d):
    s, e = 0, N-1
    while s <= e:
        m = (s+e)//2
        if lst[m] == d:
            return 1
        elif lst[m] < d:
            s = m+1
        else:
            e = m-1
    return 0


N = int(input())
lst = list(map(int, input().split()))
lst.sort()
M = int(input())
find = list(map(int, input().split()))
ans = []

for d in find:
    ans.append(binary_search(lst, d))

print(*ans, sep='\n')