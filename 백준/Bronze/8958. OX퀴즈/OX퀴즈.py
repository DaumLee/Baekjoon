N = int(input())

for _ in range(N):
    lst = input()
    sm = 0
    num = 1
    for i in range(len(lst)):
        if lst[i] == 'O':
            sm += num
            num += 1
        else:
            num = 1
    print(sm)