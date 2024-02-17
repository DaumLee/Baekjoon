N = int(input())
f = 1
cnt = 0

for i in range(1, N+1):
    f *= i

f = str(f)[::-1]

for i in range(len(f)):
    if f[i] == '0':
        cnt += 1
    else:
        break
print(cnt)