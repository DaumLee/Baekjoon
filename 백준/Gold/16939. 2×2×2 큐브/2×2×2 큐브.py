def check():
    for i in range(1, 24, 4):
        value = dice[i]
        for j in range(1, 4):
            if dice[i+j] != value:
                return False
    return True


dice = [0] + list(map(int, input().split()))
# 왼쪽
dice[1], dice[3], dice[5], dice[7], dice[9], dice[11], dice[21], dice[23] = \
dice[21], dice[23], dice[1], dice[3], dice[5], dice[7], dice[9], dice[11]
if check():
    print(1)
    exit(0)
dice[21], dice[23], dice[1], dice[3], dice[5], dice[7], dice[9], dice[11] = \
dice[1], dice[3], dice[5], dice[7], dice[9], dice[11], dice[21], dice[23]
dice[21], dice[23], dice[1], dice[3], dice[5], dice[7], dice[9], dice[11] = \
dice[1], dice[3], dice[5], dice[7], dice[9], dice[11], dice[21], dice[23]
if check():
    print(1)
    exit(0)
dice[1], dice[3], dice[5], dice[7], dice[9], dice[11], dice[21], dice[23] = \
dice[21], dice[23], dice[1], dice[3], dice[5], dice[7], dice[9], dice[11]
# 오른쪽
dice[2], dice[4], dice[6], dice[8], dice[10], dice[12], dice[21], dice[23] = \
dice[21], dice[23], dice[2], dice[4], dice[6], dice[8], dice[10], dice[12]
if check():
    print(1)
    exit(0)
dice[21], dice[23], dice[2], dice[4], dice[6], dice[8], dice[10], dice[12] = \
dice[2], dice[4], dice[6], dice[8], dice[10], dice[12], dice[21], dice[23]
dice[21], dice[23], dice[2], dice[4], dice[6], dice[8], dice[10], dice[12] = \
dice[2], dice[4], dice[6], dice[8], dice[10], dice[12], dice[21], dice[23]
if check():
    print(1)
    exit(0)
dice[2], dice[4], dice[6], dice[8], dice[10], dice[12], dice[21], dice[23] = \
dice[21], dice[23], dice[2], dice[4], dice[6], dice[8], dice[10], dice[12]
# 뒤
dice[13], dice[14], dice[5], dice[6], dice[17], dice[18], dice[21], dice[22] = \
dice[21], dice[22], dice[13], dice[14], dice[5], dice[6], dice[17], dice[18]
if check():
    print(1)
    exit(0)
dice[21], dice[22], dice[13], dice[14], dice[5], dice[6], dice[17], dice[18] = \
dice[13], dice[14], dice[5], dice[6], dice[17], dice[18], dice[21], dice[22]
dice[21], dice[22], dice[13], dice[14], dice[5], dice[6], dice[17], dice[18] = \
dice[13], dice[14], dice[5], dice[6], dice[17], dice[18], dice[21], dice[22]
if check():
    print(1)
    exit(0)
dice[13], dice[14], dice[5], dice[6], dice[17], dice[18], dice[21], dice[22] = \
dice[21], dice[22], dice[13], dice[14], dice[5], dice[6], dice[17], dice[18]
# 앞
dice[15], dice[16], dice[7], dice[8], dice[19], dice[20], dice[23], dice[24] = \
dice[23], dice[24], dice[15], dice[16], dice[7], dice[8], dice[19], dice[20]
if check():
    print(1)
    exit(0)
dice[23], dice[24], dice[15], dice[16], dice[7], dice[8], dice[19], dice[20] = \
dice[15], dice[16], dice[7], dice[8], dice[19], dice[20], dice[23], dice[24]
dice[23], dice[24], dice[15], dice[16], dice[7], dice[8], dice[19], dice[20] = \
dice[15], dice[16], dice[7], dice[8], dice[19], dice[20], dice[23], dice[24]
if check():
    print(1)
    exit(0)
dice[15], dice[16], dice[7], dice[8], dice[19], dice[20], dice[23], dice[24] = \
dice[23], dice[24], dice[15], dice[16], dice[7], dice[8], dice[19], dice[20]
# 위
dice[1], dice[2], dice[18], dice[20], dice[11], dice[12], dice[13], dice[15] = \
dice[13], dice[15], dice[1], dice[2], dice[18], dice[20], dice[11], dice[12]
if check():
    print(1)
    exit(0)
dice[13], dice[15], dice[1], dice[2], dice[18], dice[20], dice[11], dice[12] = \
dice[1], dice[2], dice[18], dice[20], dice[11], dice[12], dice[13], dice[15]
dice[13], dice[15], dice[1], dice[2], dice[18], dice[20], dice[11], dice[12] = \
dice[1], dice[2], dice[18], dice[20], dice[11], dice[12], dice[13], dice[15]
if check():
    print(1)
    exit(0)
dice[1], dice[2], dice[18], dice[20], dice[11], dice[12], dice[13], dice[15] = \
dice[13], dice[15], dice[1], dice[2], dice[18], dice[20], dice[11], dice[12]
# 아래
dice[3], dice[4], dice[17], dice[19], dice[9], dice[10], dice[14], dice[16] = \
dice[14], dice[16], dice[3], dice[4], dice[17], dice[19], dice[9], dice[10]
if check():
    print(1)
    exit(0)
dice[14], dice[16], dice[3], dice[4], dice[17], dice[19], dice[9], dice[10] = \
dice[3], dice[4], dice[17], dice[19], dice[9], dice[10], dice[14], dice[16]
dice[14], dice[16], dice[3], dice[4], dice[17], dice[19], dice[9], dice[10] = \
dice[3], dice[4], dice[17], dice[19], dice[9], dice[10], dice[14], dice[16]
if check():
    print(1)
    exit(0)
print(0)