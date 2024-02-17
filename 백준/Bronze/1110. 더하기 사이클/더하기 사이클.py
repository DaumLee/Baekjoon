a = input()

ans = int(a)
cycle = []
rtn = int()
if int(a) < 10:
    a = '0' + a

while int(rtn) != ans:
    b = str(int(a[0])+int(a[1]))
    rtn = a[-1]+b[-1]
    cycle.append(rtn)
    a = rtn

if len(cycle) == 0:
    print(1)
else:
    print(len(cycle))