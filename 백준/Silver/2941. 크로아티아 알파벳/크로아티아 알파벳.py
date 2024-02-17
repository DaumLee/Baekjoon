import sys

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

st = input()

for a in cro:
    st = st.replace(a, '0')

print(len(st))