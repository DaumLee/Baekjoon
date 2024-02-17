import math

A, B, V = map(int, input().split())

cnt = (V-A)/(A-B)
cnt = math.ceil(cnt)
print(cnt+1)