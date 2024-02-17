N = int(input())

five = N//5
three = 1

# 5로 전부 다
if not N % 5:
    print(N//5)
# 5로 해결 안되면
else:
    while five >= 0:
        if 5 * five + 3 * three == N:
            print(five + three)
            break
        elif 5 * five + 3 * three > N:
            five -= 1
            three = 1
        else:
            three += 1
    else:
        print(-1)