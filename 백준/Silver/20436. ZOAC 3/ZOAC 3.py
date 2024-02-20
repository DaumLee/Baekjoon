sl, sr = input().split()
st = input()

# 문자열과 좌표 매칭
dct = {
    'q':(0,0),'w':(0,1),'e':(0,2),'r':(0,3),'t':(0,4),'y':(0,5),'u':(0,6),'i':(0,7),'o':(0,8),'p':(0,9),
    'a':(1,0),'s':(1,1),'d':(1,2),'f':(1,3),'g':(1,4),'h':(1,5),'j':(1,6),'k':(1,7),'l':(1,8),
    'z':(2,0),'x':(2,1),'c':(2,2),'v':(2,3),'b':(2,4),'n':(2,5),'m':(2,6)
       }

# 왼손으로 누를 자판
left = [
    'q','w','e','r','t',
    'a','s','d','f','g',
    'z','x','c','v'
        ]

cl, cr = dct[sl], dct[sr]
cnt = 0

for i in range(len(st)):
    # 왼손 이동 시간
    if st[i] in left:
        cnt += abs(cl[0] - dct[st[i]][0]) + abs(cl[1] - dct[st[i]][1])
        cl = (dct[st[i]][0], dct[st[i]][1])
    # 오른손 이동 시간
    else:
        cnt += abs(cr[0] - dct[st[i]][0]) + abs(cr[1] - dct[st[i]][1])
        cr = (dct[st[i]][0], dct[st[i]][1])
    # 누르는데 걸리는 시간
    cnt += 1

print(cnt)