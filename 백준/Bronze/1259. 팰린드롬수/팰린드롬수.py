while True:
    st = input()
    if st == '0':
        break

    if st == st[::-1]:
        print('yes')
    else:
        print('no')