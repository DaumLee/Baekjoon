import sys

n = int(sys.stdin.readline())
sum = 0
score = list(map(int, sys.stdin.readline().split()))
m = max(score)

for i in range(n):
    score[i] = score[i] / m * 100
    sum += score[i]

print(sum/(len(score)))