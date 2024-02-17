import sys

l = list(map(int, sys.stdin.read().split()))

print(max(l), l.index(max(l))+1)