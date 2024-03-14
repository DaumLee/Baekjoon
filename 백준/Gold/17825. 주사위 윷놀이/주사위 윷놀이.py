def roll(v, d):
    for k in range(d):
        if v == 42:
            return v
        # 시작 말 이동
        if k == 0:
            v = start[v]
        else:
            v = middle[v]
    return v


def solve(n, s1, s2, s3, s4, score):
    global ans
    ans = max(ans, score)
    if n == 10:
        return

    # 현재 시행의 주사위 눈
    d = lst[n]

    if s1 == 42 or s1 == -1:
        s1 = -1
        e1 = -1
    else:
        e1 = roll(s1, d)
    if s2 == 42 or s2 == -1:
        s2 = -1
        e2 = -1
    else:
        e2 = roll(s2, d)
    if s3 == 42 or s3 == -1:
        s3 = -1
        e3 = -1
    else:
        e3 = roll(s3, d)
    if s4 == 42 or s4 == -1:
        s4 = -1
        e4 = -1
    else:
        e4 = roll(s4, d)

    if s1 != 42 and e1 != -1 and e1 != s2 and e1 != s3 and e1 != s4:
        if e1 == 101:
            s = 13
        elif e1 == 102:
            s = 16
        elif e1 == 103:
            s = 19
        elif e1 == 100:
            s = 25
        elif e1 == 104:
            s = 22
        elif e1 == 105:
            s = 24
        elif e1 == 106:
            s = 28
        elif e1 == 107:
            s = 27
        elif e1 == 108:
            s = 26
        elif e1 == 109:
            s = 30
        elif e1 == 110:
            s = 35
        elif e1 == 42:
            s = 0
        else:
            s = e1
        solve(n+1, e1, s2, s3, s4, score+s)
    if e2 != -1 and e2 != s1 and e2 != s3 and e2 != s4:
        if e2 == 101:
            s = 13
        elif e2 == 102:
            s = 16
        elif e2 == 103:
            s = 19
        elif e2 == 100:
            s = 25
        elif e2 == 104:
            s = 22
        elif e2 == 105:
            s = 24
        elif e2 == 106:
            s = 28
        elif e2 == 107:
            s = 27
        elif e2 == 108:
            s = 26
        elif e2 == 109:
            s = 30
        elif e2 == 110:
            s = 35
        elif e2 == 42:
            s = 0
        else:
            s = e2
        solve(n+1, s1, e2, s3, s4, score+s)
    if e3 != -1 and e3 != s1 and e3 != s2 and e3 != s4:
        if e3 == 101:
            s = 13
        elif e3 == 102:
            s = 16
        elif e3 == 103:
            s = 19
        elif e3 == 100:
            s = 25
        elif e3 == 104:
            s = 22
        elif e3 == 105:
            s = 24
        elif e3 == 106:
            s = 28
        elif e3 == 107:
            s = 27
        elif e3 == 108:
            s = 26
        elif e3 == 109:
            s = 30
        elif e3 == 110:
            s = 35
        elif e3 == 42:
            s = 0
        else:
            s = e3
        solve(n+1, s1, s2, e3, s4, score+s)
    if e4 != -1 and e4 != s1 and e4 != s2 and e4 != s3:
        if e4 == 101:
            s = 13
        elif e4 == 102:
            s = 16
        elif e4 == 103:
            s = 19
        elif e4 == 100:
            s = 25
        elif e4 == 104:
            s = 22
        elif e4 == 105:
            s = 24
        elif e4 == 106:
            s = 28
        elif e4 == 107:
            s = 27
        elif e4 == 108:
            s = 26
        elif e4 == 109:
            s = 30
        elif e4 == 110:
            s = 35
        elif e4 == 42:
            s = 0
        else:
            s = e4
        solve(n+1, s1, s2, s3, e4, score+s)


lst = list(map(int, input().split()))
# 주사위를 시작하면 도착할 칸
start = {i: i+2 for i in range(0, 41, 2)}
# 10 --> 25
start[10] = 101
start[101] = 102
start[102] = 103
start[103] = 100
# 20 --> 25
start[20] = 104
start[104] = 105
start[105] = 100
# 30 --> 25
start[30] = 106
start[106] = 107
start[107] = 108
start[108] = 100
# 100 -> 도착
start[100] = 109
start[109] = 110
start[110] = 40

middle = {i: i+2 for i in range(0, 41, 2)}
# 10 --> 25
middle[101] = 102
middle[102] = 103
middle[103] = 100
# 20 --> 25
middle[104] = 105
middle[105] = 100
# 30 --> 25
middle[106] = 107
middle[107] = 108
middle[108] = 100
# 100 -> 도착
middle[100] = 109
middle[109] = 110
middle[110] = 40

ans = 0
# 최초 시작점은 모두 0
s1 = s2 = s3 = s4 = 0
# 첫 시작점은 1번 말이 가야함
for q in range(lst[0]):
    if q == 0:
        s1 = start[s1]
    else:
        s1 = middle[s1]
solve(1, s1, s2, s3, s4, s1)
print(ans)