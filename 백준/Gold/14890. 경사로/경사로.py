def build(val, ni, nj, col=0):
    # 상하 활주로 건설
    if col:
        if ni < 0 or ni+X-1 >= N:
            return False
        for i in range(ni, ni+X):
            if arr[i][nj] != val:
                return False
            if v[i][nj] != num:
                v[i][nj] = num
            else:
                return False
    # 좌우 활주로 건설
    else:
        if nj < 0 or nj+X-1 >= N:
            return False
        for j in range(nj, nj+X):
            if arr[ni][j] != val:
                return False
            if v[ni][j] != num:
                v[ni][j] = num
            else:
                return False
    return True


def check(si, sj):
    if si >= 0:
        line = arr[si][:]
        for j in range(N-1):
            if line[j] == line[j+1]:
                continue
            # 내려가는 활주로
            elif line[j] == line[j+1]+1:
                if not build(line[j+1], si, j+1):
                    return 0
            # 올라가는 활주로
            elif line[j] == line[j+1]-1:
                if not build(line[j], si, j-X+1):
                    return 0
            else:
                return 0
    else:
        line = []
        for i in range(N):
            line.append(arr[i][sj])
        for j in range(N-1):
            if line[j] == line[j+1]:
                continue
            # 내려가는 활주로
            elif line[j] == line[j+1]+1:
                if not build(line[j+1], j+1, sj, 1):
                    return 0
            # 올라가는 활주로
            elif line[j] == line[j+1]-1:
                if not build(line[j], j-X+1, sj, 1):
                    return 0
            else:
                return 0
    return True

N, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
# v를 색칠할 번호
num = 1
ans = 0
for i in range(N):
    ans += check(i, -1)
    num += 1
    ans += check(-1, i)
    num += 1
print(ans)