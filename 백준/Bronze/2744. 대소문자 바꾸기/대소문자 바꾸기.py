st = list(map(str, input()))

for i in range(len(st)):
    if st[i].islower():
        st[i] = st[i].upper()
    else:
        st[i] = st[i].lower()

print(''.join(st))