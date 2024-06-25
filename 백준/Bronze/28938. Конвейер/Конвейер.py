_ = int(input())
sm = sum(map(int, input().split()))
if sm > 0:
    print('Right')
elif sm < 0:
    print('Left')
else:
    print('Stay')