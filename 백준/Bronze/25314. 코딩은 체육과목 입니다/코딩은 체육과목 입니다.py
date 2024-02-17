import sys

n = int(sys.stdin.read())

ans = 'long int'
for i in range(1, n // 4):
    ans = 'long ' + ans

print(ans)