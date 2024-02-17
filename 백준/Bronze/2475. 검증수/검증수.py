lst = list(map(int, input().split()))
sm = 0

for i in lst:
    sm += i**2

print(sm%10)