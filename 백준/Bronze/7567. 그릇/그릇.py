st = input()
sm = 10
for i in range(1, len(st)-1):
    if st[i] != st[i-1]:
        sm += 10
    else:
        sm += 5

if st[len(st)-1] != st[len(st)-2]:
    sm += 10
else:
    sm += 5

print(sm)