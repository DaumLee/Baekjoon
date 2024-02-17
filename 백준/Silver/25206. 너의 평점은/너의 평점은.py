import sys

sm = 0
grade = 0
score = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']
idx = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

for _ in range(20):
    lst = list(input().split())
    i = score.index(lst[2])
    if lst[2] != 'P':
        sm += float(lst[1]) * idx[i]
        grade += float(lst[1])

print(sm/grade)