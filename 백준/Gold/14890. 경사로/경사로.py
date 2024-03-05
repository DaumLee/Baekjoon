def hor(n):
    global ans

    lst = []
    for i in range(N):
        lst.append([arr[n][i], 0])

    for i in range(N-1):
        # 경사로를 둘 수 없는 경우
        if i+L >= N:
            # 다음 값과 비교
            if lst[i][0] != lst[i+1][0]:
                return
        # 경사로를 둘 수 있는 경우
        else:
            # 내리막
            if lst[i][0] > lst[i+L][0] and lst[i][0] != lst[i+1][0]:
                for j in range(i+1, i+L+1):
                    # 이미 경사로가 있으면
                    if lst[j][1]:
                        return
                    # 값이 연속하지 않으면
                    if lst[j][0]+1 != lst[i][0]:
                        return
                    lst[j][1] = 1
            # 오르막
            elif lst[i][0] < lst[i+L][0]:
                for j in range(i, i+L):
                    # 이미 경사로가 있으면
                    if lst[j][1]:
                        return
                    # 경사로를 탔을 때 값이 목적지와 다르면
                    if lst[j][0]+1 != lst[i+L][0]:
                        return
                    lst[j] = [lst[j][0]+1, 1]
            # 범위는 가능하지만 값이 같은 경우
            else:
                if lst[i][0] != lst[i+1][0]:
                    return
    ans += 1


def ver(n):
    global ans

    lst = []
    for i in range(N):
        lst.append([arr[i][n], 0])

    for i in range(N-1):
        # 경사로를 둘 수 없는 경우
        if i+L >= N:
            # 다음 값과 비교
            if lst[i][0] != lst[i+1][0]:
                return
        # 경사로를 둘 수 있는 경우
        else:
            # 내리막
            if lst[i][0] > lst[i+L][0] and lst[i][0] != lst[i+1][0]:
                for j in range(i+1, i+L+1):
                    # 이미 경사로가 있으면
                    if lst[j][1]:
                        return
                    # 값이 연속하지 않으면
                    if lst[j][0]+1 != lst[i][0]:
                        return
                    lst[j][1] = 1
            # 오르막
            elif lst[i][0] < lst[i+L][0]:
                for j in range(i, i+L):
                    # 이미 경사로가 있으면
                    if lst[j][1]:
                        return
                    # 경사로를 탔을 때 값이 목적지와 다르면
                    if lst[j][0]+1 != lst[i+L][0]:
                        return
                    lst[j] = [lst[j][0]+1, 1]
            # 범위는 가능하지만 값이 같은 경우
            else:
                if lst[i][0] != lst[i+1][0]:
                    return
    ans += 1


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    hor(i)
    ver(i)

print(ans)