import bisect

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

lst.sort()
cnts = []

for i in find:
    cnt = 0
    cnt += bisect.bisect_right(lst, i)
    cnt -= bisect.bisect_left(lst, i)
    cnts.append(cnt)

print(*cnts)