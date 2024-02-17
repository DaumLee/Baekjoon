lst = list(map(int, input().split()))

ans = 1 if lst[0] > lst[1] else 0

for i in range(7):
    if ans:
        if lst[i] < lst[i+1]:
            print('mixed')
            break
    else:
        if lst[i] > lst[i+1]:
            print('mixed')
            break
else:
    if ans:
        print('descending')
    else:
        print('ascending')