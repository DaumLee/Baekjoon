st = input()

for i in range(97,123):
    if chr(i) in st:
        print(st.count(chr(i)), end=' ')
    else:
        print(0, end=' ')