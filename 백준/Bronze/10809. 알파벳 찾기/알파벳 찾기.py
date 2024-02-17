st = input()

for i in range(97, 123):
    for j in range(len(st)):
        if st[j] == chr(i):
            print(j, end=' ')
            break
    else:
        print(-1, end=' ')