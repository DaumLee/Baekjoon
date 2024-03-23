def print_ans(MAP):
    for i in range(3):
        for j in range(3):
            print(MAP[i][j], end='')
        if i != 2:
            print()
    print()

def cubing(c):
    new_arr = [[item[:] for item in lst] for lst in arr]
    if c == 'L+':
        new_arr[0][0][0], new_arr[0][1][0], new_arr[0][2][0] = arr[3][2][2], arr[3][1][2], arr[3][0][2]
        new_arr[1][0][0], new_arr[1][1][0], new_arr[1][2][0] = arr[2][0][0], arr[2][1][0], arr[2][2][0]
        new_arr[2][0][0], new_arr[2][1][0], new_arr[2][2][0] = arr[0][0][0], arr[0][1][0], arr[0][2][0]
        new_arr[3][0][2], new_arr[3][1][2], new_arr[3][2][2] = arr[1][2][0], arr[1][1][0], arr[1][0][0]
        new_arr[4] = list(map(list, zip(*arr[4][::-1])))
    elif c == 'L-':
        new_arr[0][0][0], new_arr[0][1][0], new_arr[0][2][0] = arr[2][0][0], arr[2][1][0], arr[2][2][0]
        new_arr[1][0][0], new_arr[1][1][0], new_arr[1][2][0] = arr[3][2][2], arr[3][1][2], arr[3][0][2]
        new_arr[2][0][0], new_arr[2][1][0], new_arr[2][2][0] = arr[1][0][0], arr[1][1][0], arr[1][2][0]
        new_arr[3][0][2], new_arr[3][1][2], new_arr[3][2][2] = arr[0][2][0], arr[0][1][0], arr[0][0][0]
        new_arr[4] = list(map(list, zip(*arr[4])))[::-1]
    elif c == 'R+':
        new_arr[0][0][2], new_arr[0][1][2], new_arr[0][2][2] = arr[2][0][2], arr[2][1][2], arr[2][2][2]
        new_arr[1][0][2], new_arr[1][1][2], new_arr[1][2][2] = arr[3][2][0], arr[3][1][0], arr[3][0][0]
        new_arr[2][0][2], new_arr[2][1][2], new_arr[2][2][2] = arr[1][0][2], arr[1][1][2], arr[1][2][2]
        new_arr[3][0][0], new_arr[3][1][0], new_arr[3][2][0] = arr[0][2][2], arr[0][1][2], arr[0][0][2]
        new_arr[5] = list(map(list, zip(*arr[5][::-1])))
    elif c == 'R-':
        new_arr[0][0][2], new_arr[0][1][2], new_arr[0][2][2] = arr[3][2][0], arr[3][1][0], arr[3][0][0]
        new_arr[1][0][2], new_arr[1][1][2], new_arr[1][2][2] = arr[2][0][2], arr[2][1][2], arr[2][2][2]
        new_arr[2][0][2], new_arr[2][1][2], new_arr[2][2][2] = arr[0][0][2], arr[0][1][2], arr[0][2][2]
        new_arr[3][0][0], new_arr[3][1][0], new_arr[3][2][0] = arr[1][2][2], arr[1][1][2], arr[1][0][2]
        new_arr[5] = list(map(list, zip(*arr[5])))[::-1]
    elif c == 'U+':
        new_arr[2][0], new_arr[3][0], new_arr[4][0], new_arr[5][0],  = arr[5][0], arr[4][0], arr[2][0], arr[3][0]
        new_arr[0] = list(map(list, zip(*arr[0][::-1])))
    elif c == 'U-':
        new_arr[2][0], new_arr[3][0], new_arr[4][0], new_arr[5][0] = arr[4][0], arr[5][0], arr[3][0], arr[2][0]
        new_arr[0] = list(map(list, zip(*arr[0])))[::-1]
    elif c == 'D+':
        new_arr[2][2], new_arr[3][2], new_arr[4][2], new_arr[5][2] = arr[4][2], arr[5][2], arr[3][2],  arr[2][2]
        new_arr[1] = list(map(list, zip(*arr[1][::-1])))
    elif c == 'D-':
        new_arr[2][2], new_arr[3][2], new_arr[4][2], new_arr[5][2] = arr[5][2], arr[4][2], arr[2][2], arr[3][2]
        new_arr[1] = list(map(list, zip(*arr[1])))[::-1]
    elif c == 'F+':
        new_arr[0][2][0], new_arr[0][2][1], new_arr[0][2][2] = arr[4][2][2], arr[4][1][2], arr[4][0][2]
        new_arr[1][0][0], new_arr[1][0][1], new_arr[1][0][2] = arr[5][2][0], arr[5][1][0], arr[5][0][0]
        new_arr[4][0][2], new_arr[4][1][2], new_arr[4][2][2] = arr[1][0][0], arr[1][0][1], arr[1][0][2]
        new_arr[5][0][0], new_arr[5][1][0], new_arr[5][2][0] = arr[0][2][0], arr[0][2][1], arr[0][2][2]
        new_arr[2] = list(map(list, zip(*arr[2][::-1])))
    elif c == 'F-':
        new_arr[0][2][0], new_arr[0][2][1], new_arr[0][2][2] = arr[5][0][0], arr[5][1][0], arr[5][2][0]
        new_arr[1][0][0], new_arr[1][0][1], new_arr[1][0][2] = arr[4][0][2], arr[4][1][2], arr[4][2][2]
        new_arr[4][0][2], new_arr[4][1][2], new_arr[4][2][2] = arr[0][2][2], arr[0][2][1], arr[0][2][0]
        new_arr[5][0][0], new_arr[5][1][0], new_arr[5][2][0] = arr[1][0][2], arr[1][0][1], arr[1][0][0]
        new_arr[2] = list(map(list, zip(*arr[2])))[::-1]
    elif c == 'B+':
        new_arr[0][0][0], new_arr[0][0][1], new_arr[0][0][2] = arr[5][0][2], arr[5][1][2], arr[5][2][2]
        new_arr[1][2][0], new_arr[1][2][1], new_arr[1][2][2] = arr[4][0][0], arr[4][1][0], arr[4][2][0]
        new_arr[4][0][0], new_arr[4][1][0], new_arr[4][2][0] = arr[0][0][2], arr[0][0][1], arr[0][0][0]
        new_arr[5][0][2], new_arr[5][1][2], new_arr[5][2][2] = arr[1][2][2], arr[1][2][1], arr[1][2][0]
        new_arr[3] = list(map(list, zip(*arr[3][::-1])))
    elif c == 'B-':
        new_arr[0][0][0], new_arr[0][0][1], new_arr[0][0][2] = arr[4][2][0], arr[4][1][0], arr[4][0][0]
        new_arr[1][2][0], new_arr[1][2][1], new_arr[1][2][2] = arr[5][2][2], arr[5][1][2], arr[5][0][2]
        new_arr[4][0][0], new_arr[4][1][0], new_arr[4][2][0] = arr[1][2][0], arr[1][2][1], arr[1][2][2]
        new_arr[5][0][2], new_arr[5][1][2], new_arr[5][2][2] = arr[0][0][0], arr[0][0][1], arr[0][0][2]
        new_arr[3] = list(map(list, zip(*arr[3])))[::-1]
    return new_arr

for tc in range(int(input())):
    arr = [[['w'] * 3 for _ in range(3)]] + [[['y'] * 3 for _ in range(3)]] + [[['r'] * 3 for _ in range(3)]] + \
          [[['o'] * 3 for _ in range(3)]] + [[['g'] * 3 for _ in range(3)]] + [[['b'] * 3 for _ in range(3)]]
    N = int(input())
    rotate = list(input().split())
    for rot in rotate:
        arr = cubing(rot)
    print_ans(arr[0])