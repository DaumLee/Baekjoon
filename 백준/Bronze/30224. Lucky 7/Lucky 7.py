n = input()
if '7' in n:
    if int(n)%7:
        print(2)
    else:
        print(3)
else:
    if int(n)%7:
        print(0)
    else:
        print(1)