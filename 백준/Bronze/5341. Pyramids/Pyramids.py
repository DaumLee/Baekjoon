import sys
lst = list(map(int, sys.stdin.read().split()))
for i in range(len(lst[:-1])): print(sum(range(lst[i]+1)))