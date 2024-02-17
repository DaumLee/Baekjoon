l = []
m = []

for i in range(9):
    (*l,) = map(int, input().split())
    m.append(l)

max = m[0][0]
index = [0, 0]

for i in range(9):
    for j in range(9):
        if m[i][j] > max:
            max = m[i][j]
            index = [i, j]

print(max)
print(index[0]+1, index[1]+1)