def hor(c, ci):
    for cj in range(9):
        if arr[ci][cj] == c:
            return False
    return True

def ver(c, cj):
    for ci in range(9):
        if arr[ci][cj] == c:
            return False
    return True

def box(c, ci, cj):
    for i in range(3):
        for j in range(3):
            # 스도쿠 시작점을 분할정복으로 계산
            if arr[ci-ci%3+i][cj-cj%3+j] == c:
                return False
    return True

def check(arr):
    for i in range(9):
        for j in range(9):
            if not arr[i][j]:
                return False
    return True

def solve(n):
    if n == len(fill):
        if check(arr):
            for lst in arr:
                print(*lst, sep='')
            # 이거 안쓰고 되나?
            exit(0)
        return
    ci, cj = fill[n]
    for num in range(1, 10):
        # 넣을 수 있는 숫자면 넣어보자
        if hor(num, ci) and ver(num, cj) and box(num, ci, cj):
            # 넣고
            arr[ci][cj] = num
            solve(n+1)
            # 아니면 빼고
            arr[ci][cj] = 0

arr = []
fill = []
for i in range(9):
    lst = list(map(int, input().rstrip()))
    for j in range(9):
        if lst[j] == 0:
            fill.append((i, j))
    arr.append(lst)
# 0의 개수를 채우는 것으로 생각
solve(0)