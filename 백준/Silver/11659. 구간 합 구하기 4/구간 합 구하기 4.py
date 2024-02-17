import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
sm = deque()
sm.append(0)

for i in range(N):
    sm.append(lst[i]+sm[-1])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sm[j]-sm[i-1])