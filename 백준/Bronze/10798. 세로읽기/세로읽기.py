import sys

arr = [[0 for i in range(15)] for j in range(5)]

for i in range(5):
    ipt = list(input())
    for j in range(len(ipt)):
        arr[i][j] = ipt[j]

for i in range(15):
    for j in range(5):
        if type(arr[j][i]) == str:
            print(arr[j][i], end='')