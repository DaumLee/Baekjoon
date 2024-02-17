st = input().lower()
cnt = 0
ans = set()
for i in st:
    if cnt < st.count(i):
        cnt = st.count(i)
        ans = set(i)
    elif cnt == st.count(i):
        ans.add(i)
    st = ''.join(st.split(i))

if len(ans) == 1:
    print(ans.pop().upper())
else:
    print('?')