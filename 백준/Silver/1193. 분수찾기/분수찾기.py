X = int(input())
cnt = 0
par = 1
chd = 1
pos = -1 # -1이면 분모가 커지고 1이면 분자가 커지는 방향

while True:
    cnt += 1
    if cnt == X:
        print(f'{chd}/{par}')
        break
    if pos == -1:
        par += 1
        chd -= 1
        if chd == 0:
            chd = 1
            pos *= -1
    else:
        par -= 1
        chd += 1
        if par == 0:
            par = 1
            pos *= -1