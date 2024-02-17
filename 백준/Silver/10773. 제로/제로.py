import sys

k = int(sys.stdin.readline())

l = [0]

sum = 0

for _ in range(k):
    i = int(sys.stdin.readline())

    if i == 0:
        l.pop()
    else:
        l.append(i)

for i in range(len(l)):
    sum += l[i]

print(sum)