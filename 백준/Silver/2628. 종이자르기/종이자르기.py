row, col = map(int, input().split())
arr = [[1] * row for _ in range(col)]

N = int(input())

r = [0, row]
c = [0, col]

for _ in range(N):
    vec, num = map(int, input().split())
    if vec == 1:
        r.append(num)
    else:
        c.append(num)

r.sort()
c.sort()

mx = 0
for i in range(len(c)-1):
    height = c[i + 1] - c[i]
    for j in range(len(r)-1):
        width = r[j+1] - r[j]
        mx = max(mx, width * height)

print(mx)