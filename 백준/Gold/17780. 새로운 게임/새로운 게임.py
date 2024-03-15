from collections import defaultdict

def solve(loc):
    time = 0
    v = [[list() for _ in range(N)] for _ in range(N)]
    for i in range(1, K+1):
        si, sj = loc[i]
        v[si][sj].append(i)

    while time < 1000:
        time += 1
        for num in range(1, K+1):
            ci, cj = loc[num]
            if v[ci][cj][0] != num:
                continue
            d = stone[num]
            di, dj = delta[d]
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 2:
                for c in range(len(v[ci][cj])):
                    if v[ci][cj][c] == num:
                        move = v[ci][cj][c:]
                        for m in move:
                            loc[m] = (ni, nj)
                        if arr[ni][nj]:
                            v[ni][nj].extend(move[::-1])
                        else:
                            v[ni][nj].extend(move)
                        v[ci][cj] = v[ci][cj][:c]
                        break
                if len(v[ni][nj]) >= 4 or len(v[ci][cj]) >= 4:
                    return time
            else:
                if d == 0:
                    stone[num] = 1
                elif d == 1:
                    stone[num] = 0
                elif d == 2:
                    stone[num] = 3
                else:
                    stone[num] = 2
                new_dir = stone[num]
                rdi, rdj = delta[new_dir]
                rni, rnj = ci+rdi, cj+rdj
                if rni < 0 or rni >= N or rnj < 0 or rnj >= N or arr[rni][rnj] == 2:
                    continue
                for c in range(len(v[ci][cj])):
                    if v[ci][cj][c] == num:
                        move = v[ci][cj][c:]
                        for item in move:
                            loc[item] = (rni, rnj)
                        if arr[rni][rnj]:
                            v[rni][rnj].extend(move[::-1])
                        else:
                            v[rni][rnj].extend(move)
                        v[ci][cj] = v[ci][cj][:c]
                        break
                if len(v[rni][rnj]) >= 4 or len(v[ci][cj]) >= 4:
                    return time
    return -1

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
stone = defaultdict(int)
loc = [(0, 0)]
for i in range(1, K+1):
    si, sj, d = map(int, input().split())
    stone[i] = d-1
    loc.append((si-1, sj-1))
delta = ((0, 1), (0, -1), (-1, 0), (1, 0))

print(solve(loc))